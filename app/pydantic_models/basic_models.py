from pydantic import BaseModel
from typing import List


class ResponseMessage(BaseModel):
    description: str
    success: bool


class SupabaseItem(BaseModel):
    id: int
    name: str
    price: int


class SupabaseItems(BaseModel):
    items: List[SupabaseItem]
