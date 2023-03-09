import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()


@router.get("/")  # GET /projects/
def get_projects(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    projects = db.query(models.Project).limit(
        limit).offset(skip).all()
    return {"status": True, "detail": projects}

@router.put("/") # PUT /projects/
def add_project(payload: schemas.ProjectSchema, db: Session = Depends(get_db)):
    new_project = models.Project(**payload.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return {"status": True, "detail": new_project}