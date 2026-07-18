from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth import get_current_user

from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = UserService.create_user(db, user_data)

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "message": "User registered successfully",
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )
@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        return UserService.authenticate_user(
            db=db,
            email=user_data.email,
            password=user_data.password,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
        )
@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "is_active": current_user.is_active,
    }