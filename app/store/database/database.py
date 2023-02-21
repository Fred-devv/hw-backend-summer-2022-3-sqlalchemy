from typing import Optional, TYPE_CHECKING
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.store.database import db

if TYPE_CHECKING:
    from app.web.app import Application

#url для локальной работы
#url = "postgresql+asyncpg://postgres:762063@localhost/victorina"
#url для тестов
url = "postgresql+asyncpg://postgres:meddyson888@localhost/kts"

class Database:
    def __init__(self, app: "Application"):
        self.app = app
        self._engine: Optional[AsyncEngine] = None
        self._db: Optional[declarative_base] = None
        self.session: Optional[AsyncSession] = None

    async def connect(self, *_: list, **__: dict) -> None:
        self._db = db
        self._engine = create_async_engine(url, echo=True, future=False)
        self.session = sessionmaker(self._engine, expire_on_commit=False, future=True, class_=AsyncSession)

    async def disconnect(self, *_: list, **__: dict) -> None:
        if self._engine:
            await self._engine.dispose()
