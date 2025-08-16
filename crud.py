from typing import List
from bson import ObjectId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorCollection

from database import get_database
from schemas import ItemCreate, ItemUpdate, ItemInDB


class ItemCRUD:
    
    def __init__(self):
        self.collection_name = "items"
    
    async def get_collection(self) -> AsyncIOMotorCollection:
        db = await get_database()
        return db[self.collection_name]
    
    def _validate_object_id(self, item_id: str) -> ObjectId:
        if not ObjectId.is_valid(item_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID de item inválido"
            )
        return ObjectId(item_id)
    
    async def create(self, item_data: ItemCreate) -> ItemInDB:
        collection = await self.get_collection()
        item_dict = item_data.dict()
        
        result = await collection.insert_one(item_dict)
        created_item = await collection.find_one({"_id": result.inserted_id})
        
        if not created_item:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al crear el item"
            )
        
        return ItemInDB(**created_item)
    
    async def get_by_id(self, item_id: str) -> ItemInDB:
        collection = await self.get_collection()
        object_id = self._validate_object_id(item_id)
        
        item = await collection.find_one({"_id": object_id})
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item no encontrado"
            )
        
        return ItemInDB(**item)
    
    async def get_all(self, skip: int = 0, limit: int = 10) -> List[ItemInDB]:
        collection = await self.get_collection()
        
        skip = max(0, skip)
        limit = min(max(1, limit), 100)
        
        items = []
        cursor = collection.find().skip(skip).limit(limit)
        async for item in cursor:
            items.append(ItemInDB(**item))
        
        return items
    
    async def update(self, item_id: str, item_data: ItemUpdate) -> ItemInDB:
        collection = await self.get_collection()
        object_id = self._validate_object_id(item_id)
        
        # Solo actualizar campos que no sean None
        update_data = {k: v for k, v in item_data.dict().items() if v is not None}
        
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se proporcionaron datos para actualizar"
            )
        
        result = await collection.update_one(
            {"_id": object_id},
            {"$set": update_data}
        )
        
        if result.matched_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item no encontrado"
            )
        
        return await self.get_by_id(item_id)
    
    async def delete(self, item_id: str) -> bool:
        collection = await self.get_collection()
        object_id = self._validate_object_id(item_id)
        
        result = await collection.delete_one({"_id": object_id})
        
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item no encontrado"
            )
        
        return True
    
    async def count(self) -> int:
        collection = await self.get_collection()
        return await collection.count_documents({})


# Instancia global del CRUD
item_crud = ItemCRUD()
