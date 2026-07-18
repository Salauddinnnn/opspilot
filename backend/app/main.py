from fastapi import FastAPI
from sqlalchemy import text
from app.api.routes.incidents import router as incidents_router

from app.api.routes.auth import router as auth_router
from app.config import settings
from app.db.database import engine


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
def test_database():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("✅ Database Connected Successfully")


app.include_router(auth_router)
app.include_router(incidents_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }