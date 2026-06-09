# All CRUD endpoints.
from fastapi import APIRouter, HTTPException
from database import students_db
from schemas import Student, StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# GET ALL
@router.get("/")
def get_students():
    return students_db


# GET ONE
@router.get("/{student_id}")
def get_student(student_id: int):

    for student in students_db:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# CREATE
@router.post("/")
def create_student(student: StudentCreate):

    new_id = len(students_db) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students_db.append(new_student)

    return {
        "message": "Student created",
        "student": new_student
    }


# UPDATE
@router.put("/{student_id}")
def update_student(student_id: int, updated_student: StudentCreate):

    for student in students_db:

        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course

            return {
                "message": "Student updated",
                "student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# DELETE
@router.delete("/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students_db):

        if student["id"] == student_id:
            deleted_student = students_db.pop(index)

            return {
                "message": "Student deleted",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )