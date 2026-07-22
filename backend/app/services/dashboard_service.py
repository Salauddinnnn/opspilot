from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary(db: Session):
        return DashboardRepository.get_summary(db)

    @staticmethod
    def get_severity_summary(db: Session):
        return DashboardRepository.get_severity_summary(db)