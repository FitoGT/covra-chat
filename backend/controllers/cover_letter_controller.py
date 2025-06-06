from clients.cohere_ai import CohereAI
from fastapi import APIRouter
from dtos.cover_letters_dto import CoverLetterRequest, CoverLetterResponse


router = APIRouter(prefix="/cover-letter", tags=["Cover Letters"])
cohere_ai = CohereAI()


@router.post("/generate", response_model=CoverLetterResponse)
def generate_cover_letter(request: CoverLetterRequest):
    result = cohere_ai.generate_cover_letter(
        request.cv, request.job_description)
    return CoverLetterResponse(cover_letter=result)
