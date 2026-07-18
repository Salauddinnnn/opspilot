from pydantic import BaseModel
from pydantic import BaseModel

class IncidentCreate(BaseModel):
    title: str
    description: str | None = None
    severity: str = "medium"
class IncidentStatusUpdate(BaseModel):
    status: str    