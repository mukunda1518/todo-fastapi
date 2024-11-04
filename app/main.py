from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import todo, user


app = FastAPI()

app.include_router(todo.router)
app.include_router(user.router, prefix="/user")

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
