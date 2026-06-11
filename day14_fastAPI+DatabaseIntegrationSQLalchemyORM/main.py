from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student API"
)

# Database Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI + SQLAlchemy ORM Working"}


@app.post(
    "/students/",
    response_model=schemas.StudentResponse
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db=db, student=student)


@app.get(
    "/students/",
    response_model=list[schemas.StudentResponse]
)
def read_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


@app.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(
        db=db,
        student_id=student_id
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(
        db=db,
        student_id=student_id,
        student=student
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student

@app.delete(
    "/students/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(
        db=db,
        student_id=student_id
    )

    if not deleted_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }

@app.get(
    "/students/search/",
    response_model=list[schemas.StudentResponse]
)
def search_student(
    name: str,
    db: Session = Depends(get_db)
):
    return crud.search_student(
        db=db,
        name=name
    )
# POST     /students/
# GET      /students/
# GET      /students/{id}
# PUT      /students/{id}
# DELETE   /students/{id}
# GET      /students/search/?name=rahul