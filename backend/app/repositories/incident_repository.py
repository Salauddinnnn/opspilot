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
    def get_all(
        db: Session,
        status: str = None,
        severity: str = None,
        skip: int = 0,
        limit: int = 10,
    ):
        query = db.query(Incident)

        if status:
           query = query.filter(Incident.status == status)

        if severity:
           query = query.filter(Incident.severity == severity)

        return (
            query.order_by(Incident.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

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
    @staticmethod
    def assign_incident(
        db: Session,
        incident: Incident,
        assigned_to: int,
    ):
        incident.assigned_to = assigned_to
        db.commit()
        db.refresh(incident)
        return incident    