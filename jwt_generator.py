import jwt
import uuid
from app import settings
from datetime import datetime, timedelta

# user1 f311fc0e-4143-45d4-8649-76f36f43e65a  = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b2RvIiwic3ViIjoiZjMxMWZjMGUtNDE0My00NWQ0LTg2NDktNzZmMzZmNDNlNjVhIiwiZXhwIjoxNzE0OTkwMzE2LjU0Nzc4MiwiaWF0IjoxNzE0OTAzOTE2LjU0Nzc4Mn0.Q0XQTMcWswdodttaIUwy757d8uMTI7PQ0fn_Xw8iJsc
# user2  83c8975e-7617-4aaf-8300-c3ffa6648c4f = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b2RvIiwic3ViIjoiODNjODk3NWUtNzYxNy00YWFmLTgzMDAtYzNmZmE2NjQ4YzRmIiwiZXhwIjoxNzE0OTkwNDM5LjUzNDM4NywiaWF0IjoxNzE0OTA0MDM5LjUzNDM4N30.-ux28M3rllMEoiMwoDQcM4R5UjsNNrxp8EQ3DJza_RE

def genereate_jwt_token():
    now = datetime.now()
    payload = {
        "iss": "todo",
        "sub": "83c8975e-7617-4aaf-8300-c3ffa6648c4f",
        "exp": (now + timedelta(days=settings.TOKEN_LIFETIME)).timestamp(),
        "iat": now.timestamp(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

print(genereate_jwt_token())

