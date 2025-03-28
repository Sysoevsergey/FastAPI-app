from fastapi import FastAPI

from lifespan import lifespan


app = FastAPI(
    title="Advertisement_API",
    description="API for advertisement",
    version="0.0.1",
    lifespan=lifespan,
)

@app.get("/", tags=["Index Page"])
async def index():
    return {"message": "Index Page"}