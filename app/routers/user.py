from fastapi import APIRouter, Request, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session

from app.schemas import CreateUser, UserLogin
from app.database import get_mysql_db
from app.models import User
from app.utils import get_password_hashed, verify_password
from app.auth import genereate_jwt_token
from app.redis_client import redis_client

router = APIRouter()

@router.post("/signup")
async def register_user(request: Request, payload: CreateUser, db: Session = Depends(get_mysql_db)):
    email = payload.email
    email_check = db.query(User).filter(User.email==email).first()
    if email_check is not None:
        raise HTTPException(
            detail="Email already registered",
            status_code=status.HTTP_409_CONFLICT
        )
    hashed_password = get_password_hashed(payload.password)
    new_user = User(username =payload.username, email=payload.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    access_token = genereate_jwt_token(new_user.id)

    return {
        "message": "User registration successful",
        "data": {
            "email": new_user.email,
            "id": new_user.id,
            "access_token": access_token,
            "token_type": "bearer"
        }
    }

@router.post("/login")
async def login(request: Request, payload: UserLogin, db: Session = Depends(get_mysql_db)):
    email = payload.email
    user =  db.query(User).filter(User.email==email).first()
    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Invalid Email"
        )
    plain_password = payload.password
    if verify_password(plain_password, user.password) is False:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid Password"
        )
    access_token = genereate_jwt_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

    
@router.post("/logout")
async def logout(request: Request, ):
    bearer_token = request.headers.get("Authorization")
    if bearer_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Access Token"
        )

    # Extract token from the bearer token
    token = bearer_token.split(" ")[1].strip()

    # Add token to black list
    redis_client.setex(token, 86400, "blacklisted")

    return {"message": "Logout successful"}
