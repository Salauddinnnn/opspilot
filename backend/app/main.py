from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.routes.auth import router as auth_router
from app.api.routes.incidents import router as incidents_router
from app.api.dashboard import router as dashboard_router

from app.config import settings
from app.db.database import engine


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def test_database():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("✅ Database Connected Successfully")


# Routers
app.include_router(auth_router)
app.include_router(incidents_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }