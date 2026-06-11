from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine

import crud
import models
import schemas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student API" 
)  

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@app.get("/")
def home():
    return {
        "message": "Student Result API Running Successfully"
    }

@app.post(
    "/students/",
    response_model=schemas.StudentResponse
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(
        db,
        student
    )
@app.get(
    "/students/",
    response_model=list[
        schemas.StudentResponse
    ]
)
def get_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)

@app.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@app.put(
    "/students/{student_id}/marks",
    response_model=schemas.StudentResponse
)
def update_marks(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_marks(
        db,
        student_id,
        student.marks
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated

@app.delete(
    "/students/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_student(
        db,
        student_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message":
        "Student deleted successfully"
    }

@app.get(
    "/students/search/"
)
def search_student(
    keyword: str,
    db: Session = Depends(get_db)
):
    return crud.search_student(
        db,
        keyword
    )

@app.get(
    "/students/sort/marks"
)
def sort_students(
    db: Session = Depends(get_db)
):
    return crud.sort_students(db)