import jwt
from app.settings import SECRET_KEY


def decode_and_validate_token(access_token):
    unverified_headers = jwt.get_unverified_header(access_token)
    
    return jwt.decode(
        access_token, SECRET_KEY, algorithms=[unverified_headers["alg"]]  
    )

