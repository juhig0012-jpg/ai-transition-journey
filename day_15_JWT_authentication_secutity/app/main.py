from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session

from database import (
    Base,
    engine,
    SessionLocal
)

from models import User

from schemas import (
    SignupRequest,
    LoginRequest
)

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="JWT Authentication API"
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    return payload

@app.get("/")
def home():

    return {
        "message": "Authentication API Running"
    }

@app.post("/signup")
def signup(
    data: SignupRequest,
    db: Session = Depends(get_db)
):
    try:
        print("========== SIGNUP ==========")
        print("Username:", data.username)

        existing_user = (
            db.query(User)
            .filter(User.username == data.username)
            .first()
        )

        print("Existing User:", existing_user)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        hashed_password = hash_password(
            data.password
        )

        print("Password Hashed")

        user = User(
            username=data.username,
            password=hashed_password
        )

        db.add(user)

        print("User Added")

        db.commit()

        print("Commit Successful")

        db.refresh(user)

        print("Refresh Successful")

        return {
            "message":
            "User registered successfully"
        }

    except Exception as e:

        print("ERROR:", repr(e))

        raise

@app.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.username == data.username)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Username"
        )

    if not verify_password(
        data.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
        user.username
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get("/profile")
def profile(
    current_user=Depends(
        get_current_user
    )
):

    return {
        "message":
        "Protected Route",
        "username":
        current_user["sub"]
    }