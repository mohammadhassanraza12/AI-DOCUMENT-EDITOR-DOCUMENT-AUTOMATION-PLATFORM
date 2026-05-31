from fastapi import APIRouter, HTTPException

from app.models.item import Item

router = APIRouter()

fake_items_db = [
    {"id": 1, "name": "Document Template", "description": "Template metadata for generated documents"},
    {"id": 2, "name": "Automation Workflow", "description": "Automation workflow configuration sample"},
]


@router.get("/", response_model=list[Item])
async def read_items():
    return fake_items_db


@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = next((item for item in fake_items_db if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
