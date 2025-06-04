from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

from startup import init_db
from controllers.user_controller import router as user_router

load_dotenv()

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas e inicializar app
init_db()

# Routers modulares
app.include_router(user_router)

# LangChain + Cohere setup
llm = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model="command"
)

# Schemas locales


class CoverLetterRequest(BaseModel):
    cv: str
    job_description: str

# Endpoints legacy


@app.get("/")
def root():
    return {"message": "FastAPI + LangChain + Cohere + SQLAlchemy"}


@app.get("/generate")
def generate(pregunta: str):
    respuesta = llm([HumanMessage(content=pregunta)])
    return {"respuesta": respuesta.content}


@app.post("/generate-cover-letter")
def generate_cover_letter(request: CoverLetterRequest):
    prompt = f"""
    You are an expert cover letter writer.

    Write a concise, authentic **cover letter** that sounds like it was written by a **senior software developer with 10+ years of experience**.

    Use the following details:

    - **CV**:  
    {request.cv}

    - **Job Description**:  
    {request.job_description}

    ### Requirements:
    - Max **150 words**
    - Clear structure: *short intro, focused body, strong closing*
    - Professional tone with confidence and warmth — no fluff
    - Highlight alignment between experience and job needs
    - Avoid clichés and vague statements. Prioritize substance
    - It must sound like a real person wrote it — experienced, sharp, and to the point
    """

    response = llm([HumanMessage(content=prompt)])
    return {"cover_letter": response.content}
