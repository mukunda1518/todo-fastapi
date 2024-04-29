from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from jwt import ExpiredSignatureError, DecodeError
from fastapi.middleware.cors import CORSMiddleware


from app.routers import todo
from app.auth import decode_and_validate_token

app = FastAPI()

app.include_router(todo.router)

class AuthorizedRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.method == 'OPTIONS':
            return await call_next(request)

        bearer_token = request.headers.get('Authorization', None)
        if not bearer_token:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": "Missing Access Token",
                    "body": "Missing Access Token"
                }
            )

        try:
            auth_token = bearer_token.split(" ")[1].strip()
            token_payload = decode_and_validate_token(auth_token)
        except (ExpiredSignatureError, DecodeError) as err:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": str(err), "body": str(err)
                }
            )
        else:
            request.state.user_id = token_payload.get('sub')
            return await call_next(request)


app.add_middleware(AuthorizedRequestMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Todo Application"}
