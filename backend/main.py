from fastapi import FastAPI
from langchain_cohere import ChatCohere
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = ChatCohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    model="command"
)


class CoverLetterRequest(BaseModel):
    cv: str
    job_description: str


@app.get("/")
async def root():
    return {"message": "FastAPI + LangChain + Cohere"}


@app.get("/generate")
async def generate(pregunta: str):
    respuesta = llm([HumanMessage(content=pregunta)])
    return {"respuesta": respuesta.content}


@app.post("/generate-cover-letter")
async def generate_cover_letter(request: CoverLetterRequest):
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
