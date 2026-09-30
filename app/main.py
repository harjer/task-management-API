from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI

from app.core.config import get_settings
from app.db.session import get_db


Settings = get_settings()

app = FastAPI(
    title=Settings.app_name,
    debug=Settings.debug,
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health/db")
async def database_health(
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    await db.execute(text("SELECT 1"))

    return {"database": "ok"}
