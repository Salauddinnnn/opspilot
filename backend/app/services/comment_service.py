from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.repositories.comment_repository import CommentRepository
from app.services.audit_log_service import AuditLogService


class CommentService:

    @staticmethod
    def create_comment(
        db: Session,
        incident_id: int,
        user_id: int,
        content: str,
    ):
        comment = Comment(
            content=content,
            incident_id=incident_id,
            created_by=user_id,
        )

        saved = CommentRepository.create(
            db,
            comment,
        )

        AuditLogService.log(
            db=db,
            incident_id=incident_id,
            user_id=user_id,
            action="COMMENT_ADDED",
            details=content,
        )

        return saved

    @staticmethod
    def get_comments(
        db: Session,
        incident_id: int,
    ):
        return CommentRepository.get_by_incident(
            db,
            incident_id,
        )