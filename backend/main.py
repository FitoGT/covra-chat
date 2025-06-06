from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from startup import init_db
from controllers.user_controller import router as user_router
from controllers.cover_letter_controller import router as cover_letter
from controllers.auth_controller import router as auth_router


load_dotenv()

app = FastAPI()
FRONTEND_URL = os.getenv("FRONTEND_URL")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(user_router)
app.include_router(cover_letter)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "FastAPI + LangChain + Cohere + SQLAlchemy"}
