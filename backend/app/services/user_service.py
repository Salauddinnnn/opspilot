from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        existing_user = UserRepository.get_by_email(db, user_data.email)

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
        )

        return UserRepository.create(db, user)

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UserRepository.get_by_email(db, email)

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")
        if not user.is_active:
            raise ValueError("User account is inactive")    

        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "email": user.email,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }