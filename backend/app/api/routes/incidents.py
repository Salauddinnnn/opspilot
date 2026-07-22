from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_user,
    require_admin,
)
from app.db.session import get_db

from app.schemas.incident import (
    IncidentCreate,
    IncidentStatusUpdate,
    IncidentAnalysisResponse,
    IncidentAssign,
    IncidentResponse,
)
from app.schemas.comment import (
    CommentCreate,
    CommentResponse,
)
from app.schemas.audit_log import AuditLogResponse

from app.services.incident_service import IncidentService
from app.services.comment_service import CommentService
from app.services.audit_log_service import AuditLogService


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.get("/")
def get_incidents(
    status: str = None,
    severity: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return IncidentService.get_all_incidents(
        db=db,
        status=status,
        severity=severity,
        skip=skip,
        limit=limit,
    )


@router.post(
    "/",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
)
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


@router.patch(
    "/{incident_id}/status",
    response_model=IncidentResponse,
)
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

@router.patch(
    "/{incident_id}/assign",
    response_model=IncidentResponse,
)
def assign_incident(
    incident_id: int,
    assign_data: IncidentAssign,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin),
):
    incident = IncidentService.assign_incident(
        db=db,
        incident_id=incident_id,
        assigned_to=assign_data.assigned_to,
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
    current_user=Depends(require_admin),
):
    deleted = IncidentService.delete_incident(db, incident_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )
@router.post(
    "/{incident_id}/analyze",
    response_model=IncidentAnalysisResponse,
)
def analyze_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    analysis = IncidentService.analyze_incident(
        db=db,
        incident_id=incident_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return analysis
@router.post(
    "/{incident_id}/comments",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(
    incident_id: int,
    comment_data: CommentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incident = IncidentService.get_incident_by_id(
        db,
        incident_id,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return CommentService.create_comment(
        db=db,
        incident_id=incident_id,
        user_id=current_user.id,
        content=comment_data.content,
    )


@router.get(
    "/{incident_id}/comments",
    response_model=list[CommentResponse],
)
def get_comments(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incident = IncidentService.get_incident_by_id(
        db,
        incident_id,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return CommentService.get_comments(
        db=db,
        incident_id=incident_id,
    )
@router.get(
    "/{incident_id}/audit-logs",
    response_model=list[AuditLogResponse],
)
def get_audit_logs(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    incident = IncidentService.get_incident_by_id(
        db,
        incident_id,
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return AuditLogService.get_logs(
        db=db,
        incident_id=incident_id,
    )                