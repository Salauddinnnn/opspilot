from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.session import get_db
from app.schemas.incident import IncidentCreate, IncidentStatusUpdate
from app.services.incident_service import IncidentService


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.get("/")
def get_incidents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return IncidentService.get_all_incidents(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_incident(
    incident_data: IncidentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return IncidentService.create_incident(
        db=db,
        incident_data=incident_data,
        user_id=current_user.id,
    )


@router.get("/{incident_id}")
def get_incident_by_id(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incident = IncidentService.get_incident_by_id(db, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident


@router.patch("/{incident_id}/status")
def update_incident_status(
    incident_id: int,
    status_data: IncidentStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incident = IncidentService.update_incident_status(
        db=db,
        incident_id=incident_id,
        status_data=status_data,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident


@router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    deleted = IncidentService.delete_incident(db, incident_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )