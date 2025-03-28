from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import init_orm, close_orm


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_orm()
    print("start")
    yield
    await close_orm()
    print("close")
