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


def get_student(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentUpdate
):
    db_student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if not db_student:
        return None

    db_student.name = student.name
    db_student.marks = student.marks

    db.commit()

    db.refresh(db_student)

    return db_student

def delete_student(
    db: Session,
    student_id: int
):
    db_student = (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )

    if not db_student:
        return None

    db.delete(db_student)

    db.commit()

    return db_student

def search_student(
    db: Session,
    name: str
):
    return (
        db.query(models.Student)
        .filter(models.Student.name.ilike(f"%{name}%"))
        .all()
    )