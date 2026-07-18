from fastapi import FastAPI
from app.api.routes import router
from app.config import settings
from sqlalchemy import text
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
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }