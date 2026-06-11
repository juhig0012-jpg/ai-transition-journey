from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name: str
    marks: int

class StudentUpdate(BaseModel):
    name: str
    marks: int

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )