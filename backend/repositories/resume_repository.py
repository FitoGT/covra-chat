from sqlalchemy.orm import Session
from models.resume import Resume
from uuid import UUID
from typing import List


class ResumeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_resumes_by_user(self, user_id: UUID) -> List[Resume]:

        return (
            self.db.query(Resume)
            .filter(Resume.user_id == user_id)
            .all()
        )

    def create_resume(self, user_id: UUID, resume_text: str) -> Resume:

        new_resume = Resume(
            user_id=user_id,
            resume=resume_text
        )
        self.db.add(new_resume)
        self.db.commit()
        self.db.refresh(new_resume)
        return new_resume
