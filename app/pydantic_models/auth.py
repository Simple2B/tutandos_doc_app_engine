#  from typing import Optional
from pydantic import BaseModel, Field


class FirebaseToken(BaseModel):
    id_token: str = Field("Firebase id token")
