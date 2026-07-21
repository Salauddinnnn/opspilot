from datetime import datetime

from pydantic import BaseModel


class AuditLogResponse(BaseModel):
    id: int
    incident_id: int
    user_id: int
    action: str
    details: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }