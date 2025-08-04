from pydantic import BaseModel
from uuid import UUID
from typing import List


class ResumeDto(BaseModel):
    id: UUID
    user_id: UUID
    resume: str

    model_config = {
        "from_attributes": True
    }


class ResumesDto(BaseModel):
    resumes: List[ResumeDto]


class ResumeResponseDto(BaseModel):
    message: str
