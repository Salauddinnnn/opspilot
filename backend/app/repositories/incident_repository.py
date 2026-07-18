from sqlalchemy.orm import Session

from app.models.incident import Incident


class IncidentRepository:

    @staticmethod
    def create(db: Session, incident: Incident):
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident

    @staticmethod
    def get_all(db: Session):
        return db.query(Incident).order_by(
            Incident.created_at.desc()
        ).all()
        