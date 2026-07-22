from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.session import get_db

from app.schemas.dashboard import (
    DashboardSummary,
    SeveritySummary,
)
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardSummary,
)
def get_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DashboardService.get_summary(db)


@router.get(
    "/severity",
    response_model=SeveritySummary,
)
def get_severity(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DashboardService.get_severity_summary(db)