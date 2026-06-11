from sqlalchemy.orm import Session

import models
import schemas
def create_student(
    db: Session,
    student: schemas.StudentCreate
):
    db_student = models.Student(
        name=student.name,
        marks=student.marks
    )

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(
    db: Session,
    student_id: int
):
    return (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

def update_marks(
    db: Session,
    student_id: int,
    marks: int
):
    student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if not student:
        return None

    student.marks = marks

    db.commit()

    db.refresh(student)

    return student

def delete_student(
    db: Session,
    student_id: int
):
    student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if not student:
        return None

    db.delete(student)

    db.commit()

    return student

def search_student(
    db: Session,
    keyword: str
):
    return (
        db.query(models.Student)
        .filter(
            models.Student.name.ilike(
                f"%{keyword}%"
            )
        )
        .all()
    )

def sort_students(
    db: Session
):
    return (
        db.query(models.Student)
        .order_by(
            models.Student.marks.desc()
        )
        .all()
    )