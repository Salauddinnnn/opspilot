from sqlalchemy.orm import Session

from app.core.security import hash_password
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