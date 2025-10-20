# init_user.py
from database import engine, SessionLocal, Base
import models

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def create_user():
    db = SessionLocal()
    username = "admin"
    password = "admin123"

    existing_user = db.query(models.User).filter_by(username=username).first()
    if not existing_user:
        new_user = models.User(username=username, password=password)
        db.add(new_user)
        db.commit()
        print(f"✅ User '{username}' created successfully.")
    else:
        print(f"⚠ User '{username}' already exists.")

if __name__ == "__main__":
    create_user()