from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.repositories.incident_repository import IncidentRepository
from app.schemas.incident import IncidentCreate, IncidentStatusUpdate


class IncidentService:

    @staticmethod
    def create_incident(
        db: Session,
        incident_data: IncidentCreate,
        user_id: int,
    ):
        incident = Incident(
            title=incident_data.title,
            description=incident_data.description,
            severity=incident_data.severity,
            created_by=user_id,
        )

        return IncidentRepository.create(db, incident)

    @staticmethod
    def get_all_incidents(db: Session):
        return IncidentRepository.get_all(db)

    @staticmethod
    def get_incident_by_id(db: Session, incident_id: int):
        return IncidentRepository.get_by_id(db, incident_id)

    @staticmethod
    def update_incident_status(
        db: Session,
        incident_id: int,
        status_data: IncidentStatusUpdate,
    ):
        incident = IncidentRepository.get_by_id(db, incident_id)

        if not incident:
            return None

        return IncidentRepository.update_status(
            db,
            incident,
            status_data.status,
        )

    @staticmethod
    def delete_incident(
        db: Session,
        incident_id: int,
    ):
        incident = IncidentRepository.get_by_id(db, incident_id)

        if not incident:
            return False

        IncidentRepository.delete(db, incident)
        return True