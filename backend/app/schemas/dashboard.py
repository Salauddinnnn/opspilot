from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total: int
    open: int
    in_progress: int
    resolved: int


class SeveritySummary(BaseModel):
    critical: int
    high: int
    medium: int
    low: int