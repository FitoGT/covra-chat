from sqlalchemy.orm import Session
from repositories.resume_repository import ResumeRepository
from models.resume import Resume
from uuid import UUID
from typing import List
from PyPDF2 import PdfReader
from docx import Document
import io


class ResumeService:
    def __init__(self, db: Session):
        self.repo = ResumeRepository(db)

    def get_user_resumes(self, user_id: UUID) -> List[Resume]:
        return self.repo.get_resumes_by_user(user_id)

    def create_user_resume(self, user_id: UUID, resume_text: str) -> Resume:
        return self.repo.create_resume(user_id, resume_text)

    def process_resume_file(self, user_id: UUID, contents: bytes, content_type: str) -> None:

        if content_type == "text/plain":
            text_resume = contents.decode("utf-8", errors="ignore")
        else:
            text_resume = self._extract_text_from_file(contents, content_type)

        self.create_user_resume(user_id, text_resume)

    def _extract_text_from_file(self, contents: bytes, content_type: str) -> str:

        if content_type == "application/pdf":
            pdf = PdfReader(io.BytesIO(contents))
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

        elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(io.BytesIO(contents))
            return "\n".join(p.text for p in doc.paragraphs)

        else:
            return ""
