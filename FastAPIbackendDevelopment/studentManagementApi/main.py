# register router
from fastapi import FastAPI
from routers.students import router as student_router

app = FastAPI(
    title="Student Management API"
)

app.include_router(student_router)

@app.get("/")
def home():
    return {
        "message": "Student Management API Running"
    }
# Test URLs
# Home
# GET http://127.0.0.1:8000/
# Get All Students
# GET http://127.0.0.1:8000/students/
# Get Student
# GET http://127.0.0.1:8000/students/1
# Create Student
# POST http://127.0.0.1:8000/students/

# Body:

# {
#   "name": "Amit",
#   "age": 23,
#   "course": "FastAPI"
# }
# Update Student
# PUT http://127.0.0.1:8000/students/1

# Body:

# {
#   "name": "Rahul Sharma",
#   "age": 22,
#   "course": "Python Advanced"
# }
# Delete Student
# DELETE http://127.0.0.1:8000/students/1
# Swagger Documentation
# http://127.0.0.1:8000/docs