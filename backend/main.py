from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

from startup import init_db
from controllers.user_controller import router as user_router
from controllers.cover_letter_controller import router as cover_letter_controller

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
app.include_router(cover_letter_controller)


@app.get("/")
def root():
    return {"message": "FastAPI + LangChain + Cohere + SQLAlchemy"}
