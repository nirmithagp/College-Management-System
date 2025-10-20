from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from schemas import CollegeCreate, CollegeUpdate
from database import get_db

router = APIRouter()

@router.get("/colleges/", response_model=List[CollegeUpdate])
def read_colleges(db: Session = Depends(get_db)):
    return db.query(models.College).all()

@router.post("/colleges/", response_model=CollegeUpdate)
def create_college(college: CollegeCreate, db: Session = Depends(get_db)):
    new_college = models.College(**college.dict())
    db.add(new_college)
    db.commit()
    db.refresh(new_college)
    return new_college

@router.get("/colleges/{college_id}", response_model=CollegeUpdate)
def get_college(college_id: int, db: Session = Depends(get_db)):
    college = db.query(models.College).get(college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college

@router.put("/colleges/{college_id}", response_model=CollegeUpdate)
def update_college(college_id: int, college: CollegeCreate, db: Session = Depends(get_db)):
    db_college = db.query(models.College).get(college_id)
    if not db_college:
        raise HTTPException(status_code=404, detail="College not found")
    for key, value in college.dict().items():
        setattr(db_college, key, value)
    db.commit()
    db.refresh(db_college)
    return db_college

@router.delete("/colleges/{college_id}")
def delete_college(college_id: int, db: Session = Depends(get_db)):
    college = db.query(models.College).get(college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    db.delete(college)
    db.commit()
    return {"detail": "College deleted"}