import jwt
import uuid
from app import settings
from datetime import datetime, timedelta

# user1 - 681a5c91-8e15-4657-b1bf-2e5c07576250 : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b2RvIiwic3ViIjoiNjgxYTVjOTEtOGUxNS00NjU3LWIxYmYtMmU1YzA3NTc2MjUwIiwiZXhwIjoxNzE4NTQ4OTYwLjkyMTU0MywiaWF0IjoxNzE3MjUyOTYwLjkyMTU0M30.Ek8kb0YsC7ee7YzlePWK7WdNxYdnvzXbWTpWobn3G3s
# user2 - d6a6f6aa-81af-4a63-8c97-766aca39e011 : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b2RvIiwic3ViIjoiZDZhNmY2YWEtODFhZi00YTYzLThjOTctNzY2YWNhMzllMDExIiwiZXhwIjoxNzE4NTQ4OTg2Ljg5ODkyMywiaWF0IjoxNzE3MjUyOTg2Ljg5ODkyM30.LNHPrHbwUyydQFclzLUa5hnQV8tihKEWFgmvQG_3NxA
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

