from sqlalchemy.orm import Session

from app.models.incident import Incident
from app.repositories.incident_repository import IncidentRepository
from app.schemas.incident import (
    IncidentCreate,
    IncidentStatusUpdate,
    IncidentAnalysisResponse,
)
from app.services.ai_service import AIService
from app.services.audit_log_service import AuditLogService


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

        incident = IncidentRepository.create(
            db,
            incident,
        )

        AuditLogService.log(
            db=db,
            incident_id=incident.id,
            user_id=user_id,
            action="INCIDENT_CREATED",
            details=f"Created incident '{incident.title}'",
        )

        return incident

    @staticmethod
    def get_all_incidents(
        db: Session,
        status: str = None,
        severity: str = None,
        skip: int = 0,
        limit: int = 10,
    ):
        return IncidentRepository.get_all(
            db=db,
            status=status,
            severity=severity,
            skip=skip,
            limit=limit,
        )

    @staticmethod
    def get_incident_by_id(
        db: Session,
        incident_id: int,
    ):
        return IncidentRepository.get_by_id(
            db,
            incident_id,
        )

    @staticmethod
    def update_incident_status(
        db: Session,
        incident_id: int,
        status_data: IncidentStatusUpdate,
    ):
        incident = IncidentRepository.get_by_id(
            db,
            incident_id,
        )

        if not incident:
            return None

        updated = IncidentRepository.update_status(
            db,
            incident,
            status_data.status,
        )

        AuditLogService.log(
            db=db,
            incident_id=incident.id,
            user_id=incident.created_by,
            action="STATUS_CHANGED",
            details=f"Status changed to {status_data.status}",
        )

        return updated

    @staticmethod
    def assign_incident(
        db: Session,
        incident_id: int,
        assigned_to: int,
    ):
        incident = IncidentRepository.get_by_id(
            db,
            incident_id,
        )

        if not incident:
            return None

        assigned = IncidentRepository.assign_incident(
            db=db,
            incident=incident,
            assigned_to=assigned_to,
        )

        AuditLogService.log(
            db=db,
            incident_id=incident.id,
            user_id=incident.created_by,
            action="INCIDENT_ASSIGNED",
            details=f"Assigned to user {assigned_to}",
        )

        return assigned

    @staticmethod
    def delete_incident(
        db: Session,
        incident_id: int,
    ):
        incident = IncidentRepository.get_by_id(
            db,
            incident_id,
        )

        if not incident:
            return False

        IncidentRepository.delete(
            db,
            incident,
        )

        return True

    @staticmethod
    def analyze_incident(
        db: Session,
        incident_id: int,
    ):
        incident = IncidentRepository.get_by_id(
            db,
            incident_id,
        )

        if not incident:
            return None

        analysis = AIService.analyze_incident(
            title=incident.title,
            description=incident.description or "",
            severity=incident.severity,
        )

        return IncidentAnalysisResponse.model_validate_json(
            analysis
        )