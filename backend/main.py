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
    prompt = f"""You are a professional cover letter writer.
        Generate a short, impactful and friendly cover letter based on the following:
            
        CV:
        {request.cv}

        Job Description:
        {request.job_description}
        Keep the letter concise — no more than **150 words**. 
        Focus on aligning the candidate's experience with the job requirements.
        Use a professional but energetic tone.
        Structure it clearly with a brief intro, body, and closing.
        Avoid clichés and overly generic phrases."""

    response = llm([HumanMessage(content=prompt)])
    return {"cover_letter": response.content}
