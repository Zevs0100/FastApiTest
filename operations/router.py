from dataclasses import Field

from fastapi import APIRouter
from pydantic import BaseModel

arr = 123
router = APIRouter(
    prefix = "/operations",
    tags = ["Operation"]
)

@router.get("/")
async def get_operations():
    return {"messege, hi"}


