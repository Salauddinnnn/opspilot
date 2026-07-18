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

    @staticmethod
    def get_by_id(db: Session, incident_id: int):
        return db.query(Incident).filter(
            Incident.id == incident_id
        ).first()

    @staticmethod
    def update_status(
        db: Session,
        incident: Incident,
        status: str,
    ):
        incident.status = status
        db.commit()
        db.refresh(incident)
        return incident

    @staticmethod
    def delete(
        db: Session,
        incident: Incident,
    ):
        db.delete(incident)
        db.commit()