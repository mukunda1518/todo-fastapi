import jwt
import datetime
from app.redis_client import redis_client
from jwt import ExpiredSignatureError, DecodeError
from fastapi import Request, HTTPException, status

from app.settings import SECRET_KEY, TOKEN_LIFETIME


def genereate_jwt_token(user_id):
    now = datetime.datetime.now()
    payload = {
        "iss": "todo-app",
        "sub": user_id,
        "exp": (now + datetime.timedelta(days=int(TOKEN_LIFETIME))).timestamp(),
        "iat": now.timestamp(),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_and_validate_token(access_token):
    # Check if the token is blacklisted in Redis
    if redis_client.exists(access_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been logged out"
        )
    unverified_headers = jwt.get_unverified_header(access_token)
    return jwt.decode(
        access_token, SECRET_KEY, algorithms=[unverified_headers["alg"]]  
    )

async def validate_token(request: Request):
    bearer_token = request.headers.get('Authorization', None)
    if not bearer_token:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Missing Access Token"
        )
    try:
        auth_token = bearer_token.split(" ")[1].strip()
        token_payload = decode_and_validate_token(auth_token)
        request.state.user_id = token_payload.get("sub")
        return token_payload
    except (ExpiredSignatureError, DecodeError) as err:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= str(err)
        )
