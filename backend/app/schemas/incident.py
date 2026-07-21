from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class IncidentCreate(BaseModel):
    title: str
    description: str | None = None
    severity: str = "medium"


class IncidentStatusUpdate(BaseModel):
    status: str


class IncidentAssign(BaseModel):
    assigned_to: int


class IncidentFilter:
    def __init__(
        self,
        status: Optional[str] = None,
        severity: Optional[str] = None,
        skip: int = 0,
        limit: int = 10,
    ):
        self.status = status
        self.severity = severity
        self.skip = skip
        self.limit = limit


class IncidentAnalysisResponse(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: str
    prevention: str


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str | None
    severity: str
    status: str
    created_by: int
    assigned_to: int | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)