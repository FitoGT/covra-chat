from clients.cohere_ai import CohereAI
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/cover-letter", tags=["Cover Letters"])
cohere_ai = CohereAI()


class CoverLetterRequest(BaseModel):
    cv: str
    job_description: str


@router.post("/generate")
def generate_cover_letter(request: CoverLetterRequest):
    result = cohere_ai.generate_cover_letter(
        request.cv, request.job_description)
    return {"cover_letter": result}
