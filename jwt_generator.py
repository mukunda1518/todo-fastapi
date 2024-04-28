import jwt
import uuid
from app import settings
from datetime import datetime, timedelta


def genereate_jwt_token():
    now = datetime.now()
    payload = {
        "iss": "todo",
        "sub": str(uuid.uuid4()),
        "exp": (now + timedelta(days=settings.TOKEN_LIFETIME)).timestamp(),
        "iat": now.timestamp(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

print(genereate_jwt_token())

