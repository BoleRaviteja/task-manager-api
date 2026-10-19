
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import initialize_database
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="Task Manager API",
    lifespan=lifespan,
)

app.include_router(router)
