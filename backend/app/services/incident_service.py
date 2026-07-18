from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.repositories.incident_repository import IncidentRepository
from app.schemas.incident import IncidentCreate


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