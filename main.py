from database import Base, engine  # ✅ Correct import
from fastapi import FastAPI, HTTPException, Query
from schemas import CollegeCreate, CollegeUpdate
from college_storage import CollegeStorage
from pydantic import BaseModel
from models import User

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  # You can replace "*" with ["http://localhost:5500"] or your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

college_storage = CollegeStorage()

# Dummy login schema
class LoginRequest(BaseModel):
    username: str
    password: str
    role: str

@app.post("/login")
def login(request: LoginRequest):
    if request.role == "admin" and request.username == "admin" and request.password == "admin123":
        return {"message": "Welcome Admin!", "role": "admin"}
    elif request.role == "user" and request.username == "user" and request.password == "user123":
        return {"message": "Welcome User!", "role": "user"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/")
def root():
    return {"message": "College API is running!"}

@app.get("/colleges/")
async def get_all_colleges():
    return await college_storage.get_all_colleges()

@app.get("/colleges/{college_id}")
async def get_college(college_id: str):
    college = await college_storage.get_college(college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college

@app.post("/colleges/")
async def create_college(college: CollegeCreate):
    return await college_storage.create_college(college)

@app.put("/colleges/{college_id}")
async def update_college(college_id: str, college: CollegeUpdate):
    updated = await college_storage.update_college(college_id, college)
    if not updated:
        raise HTTPException(status_code=404, detail="College not found")
    return updated

@app.delete("/colleges/{college_id}")
async def delete_college(college_id: str):
    success = await college_storage.delete_college(college_id)
    if not success:
        raise HTTPException(status_code=404, detail="College not found")
    return {"message": "College deleted successfully"}

@app.get("/search/")
async def search_colleges(
    query: str = Query(default=""),
    type_filter: str = Query(default=""),
    location_filter: str = Query(default="")
):
    return await college_storage.search_colleges(query, type_filter, location_filter)




