import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()


@router.get("/")  # /projects/
def get_projects(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    projects = db.query(models.Projects).limit(
        limit).offset(skip).all()
    return {"status": True, "detail": projects}
