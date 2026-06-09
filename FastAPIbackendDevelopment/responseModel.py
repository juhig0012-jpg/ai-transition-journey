from fastapi import FastAPI
from pydantic import BaseModel

class StudentResponse(BaseModel):
    name: str

class Student(BaseModel):
    name: str
    age: int
    email: str

app = FastAPI()

@app.post("/student", response_model=StudentResponse)
def create_student(student: Student):

    return student