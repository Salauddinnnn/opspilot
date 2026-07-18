from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.session import get_db
from app.schemas.incident import IncidentCreate
from app.services.incident_service import IncidentService


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_incident(
    incident_data: IncidentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        incident = IncidentService.create_incident(
            db=db,
            incident_data=incident_data,
            user_id=current_user.id,
        )

        return {
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "status": incident.status,
            "created_by": incident.created_by,
            "created_at": incident.created_at,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )
@router.get("/")
def get_incidents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incidents = IncidentService.get_all_incidents(db)

    return [
        {
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "status": incident.status,
            "created_by": incident.created_by,
            "created_at": incident.created_at,
        }
        for incident in incidents
    ]   