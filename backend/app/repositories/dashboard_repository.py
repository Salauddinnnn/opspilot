from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.incident import Incident


class DashboardRepository:

    @staticmethod
    def get_summary(db: Session):
        total = db.query(Incident).count()

        open_count = db.query(Incident).filter(
            Incident.status == "open"
        ).count()

        in_progress = db.query(Incident).filter(
            Incident.status == "in_progress"
        ).count()

        resolved = db.query(Incident).filter(
            Incident.status == "resolved"
        ).count()

        return {
            "total": total,
            "open": open_count,
            "in_progress": in_progress,
            "resolved": resolved,
        }

    @staticmethod
    def get_severity_summary(db: Session):
        rows = (
            db.query(
                Incident.severity,
                func.count(Incident.id),
            )
            .group_by(Incident.severity)
            .all()
        )

        data = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
        }

        for severity, count in rows:
            data[severity] = count

        return data