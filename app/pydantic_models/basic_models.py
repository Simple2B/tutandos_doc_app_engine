from datetime import datetime
from pydantic import BaseModel
from typing import List


class ResponseMessage(BaseModel):
    description: str
    success: bool


class SupabaseItem(BaseModel):
    id: int
    name: str
    price: int
    created_at: datetime


class SupabaseItems(BaseModel):
    key: List[SupabaseItem]
