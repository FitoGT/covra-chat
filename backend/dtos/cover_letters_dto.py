from pydantic import BaseModel


class CoverLetterRequest(BaseModel):
    cv: str
    job_description: str
