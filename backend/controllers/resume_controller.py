from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from db.database import get_db
from services.resume_service import ResumeService
from utils.auth import get_current_user
from fastapi.security import HTTPBearer
from models.user import User
from dtos.resume_dto import ResumeResponseDto, ResumesDto, ResumeDto

security = HTTPBearer()

router = APIRouter(prefix="/resumes", tags=["Resumes"])


@router.get("/", response_model=ResumesDto)
def get_resumes_by_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = ResumeService(db)
    resumes = service.get_user_resumes(current_user.id)

    resume_dtos = [ResumeDto.model_validate(resume) for resume in resumes]
    return ResumesDto(resumes=resume_dtos)


@router.post("/", status_code=status.HTTP_202_ACCEPTED, response_model=ResumeResponseDto)
async def create_resume(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if file.content_type not in [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]:
        raise HTTPException(status_code=400, detail="Invalid file type.")

    contents = await file.read()
    service = ResumeService(db)
    background_tasks.add_task(
        service.process_resume_file, current_user.id, contents, file.content_type)

    return ResumeResponseDto(message="Resume is being processed in the background.")
