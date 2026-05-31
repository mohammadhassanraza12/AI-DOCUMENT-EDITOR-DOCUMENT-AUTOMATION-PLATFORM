from fastapi import FastAPI

from app.routers import items

app = FastAPI(title="AI Document Editor Backend")

app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/")
async def root():
    return {"message": "AI Document Editor Backend is running"}
