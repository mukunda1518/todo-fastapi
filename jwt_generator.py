import jwt
import uuid
from app import settings
from datetime import datetime, timedelta

def genereate_jwt_token():
    now = datetime.now()
    payload = {
        "iss": "todo",
        "sub": "d6a6f6aa-81af-4a63-8c97-766aca39e011",
        "exp": (now + timedelta(days=int(settings.TOKEN_LIFETIME))).timestamp(),
        "iat": now.timestamp(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

print(genereate_jwt_token())

