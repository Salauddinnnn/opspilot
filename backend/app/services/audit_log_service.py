from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog
from app.repositories.audit_log_repository import AuditLogRepository


class AuditLogService:

    @staticmethod
    def log(
        db: Session,
        incident_id: int,
        user_id: int,
        action: str,
        details: str | None = None,
    ):
        log = AuditLog(
            incident_id=incident_id,
            user_id=user_id,
            action=action,
            details=details,
        )

        return AuditLogRepository.create(
            db=db,
            log=log,
        )

    @staticmethod
    def get_logs(
        db: Session,
        incident_id: int,
    ):
        return AuditLogRepository.get_by_incident(
            db=db,
            incident_id=incident_id,
        )