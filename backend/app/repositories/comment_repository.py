from sqlalchemy.orm import Session

from app.models.comment import Comment


class CommentRepository:

    @staticmethod
    def create(
        db: Session,
        comment: Comment,
    ):
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    @staticmethod
    def get_by_incident(
        db: Session,
        incident_id: int,
    ):
        return (
            db.query(Comment)
            .filter(Comment.incident_id == incident_id)
            .order_by(Comment.created_at.asc())
            .all()
        )