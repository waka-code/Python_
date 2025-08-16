from typing import Optional
from pydantic import BaseModel, Field, validator
from models import MongoBaseModel


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del item")
    description: Optional[str] = Field(None, max_length=500, description="Descripción opcional")
    
    @validator('name')
    def validate_name(cls, v: str) -> str:
        return v.strip()
    
    @validator('description')
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        if v:
            return v.strip()
        return v

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    
    @validator('name')
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        if v:
            return v.strip()
        return v
    
    @validator('description')
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        if v:
            return v.strip()
        return v


class ItemInDB(MongoBaseModel, ItemBase):
    pass


class ItemResponse(ItemBase):
    id: str = Field(..., description="ID único del item")
    
class ItemCreate(ItemBase):
    pass