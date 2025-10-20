from sqlalchemy.orm import Session
from models import College
from schemas import CollegeCreate

# Create
def create_college(db: Session, college: CollegeCreate):
    db_college = College(name=college.name, district=college.district)
    db.add(db_college)
    db.commit()
    db.refresh(db_college)
    return db_college

# Read all
def get_colleges(db: Session, skip: int = 0, limit: int = 10):
    return db.query(College).offset(skip).limit(limit).all()

# Read by ID
def get_college(db: Session, college_id: int):
    return db.query(College).filter(College.id == college_id).first()

# Delete
def delete_college(db: Session, college_id: int):
    college = db.query(College).filter(College.id == college_id).first()
    if college:
        db.delete(college)
        db.commit()
    return college

