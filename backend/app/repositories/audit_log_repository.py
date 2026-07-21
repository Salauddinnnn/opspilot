from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditLogRepository:

    @staticmethod
    def create(
        db: Session,
        log: AuditLog,
    ):
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    @staticmethod
    def get_by_incident(
        db: Session,
        incident_id: int,
    ):
        return (
            db.query(AuditLog)
            .filter(AuditLog.incident_id == incident_id)
            .order_by(AuditLog.created_at.desc())
            .all()
        )