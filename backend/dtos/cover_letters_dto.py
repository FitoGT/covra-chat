from pydantic import BaseModel


class CoverLetterRequest(BaseModel):
    cv: str
    job_description: str


class CoverLetterResponse(BaseModel):
    cover_letter: str
