from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: Any
    name: str
    contact_info: str
    created_at: Any


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_info: str
    created_at: Any
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int
    name: str
    contact_info: str
    created_at: str

    class Config:
        from_attributes = True

