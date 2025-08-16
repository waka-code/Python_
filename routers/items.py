from typing import List
from fastapi import APIRouter, status, Query, Path

from schemas import ItemCreate, ItemUpdate, ItemResponse
from crud import item_crud

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item no encontrado"}}
)


@router.post(
    "/",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo item",
    description="Crea un nuevo item en la base de datos"
)
async def create_item(item: ItemCreate) -> ItemResponse:
    created_item = await item_crud.create(item)
    return ItemResponse(
        id=str(created_item.id),
        name=created_item.name,
        description=created_item.description
    )


@router.get(
    "/",
    response_model=List[ItemResponse],
    summary="Listar items",
    description="Obtiene una lista paginada de items"
)
async def list_items(
    skip: int = Query(0, ge=0, description="Número de items a omitir"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de items a retornar")
) -> List[ItemResponse]:
    """Obtener lista de items con paginación."""
    items = await item_crud.get_all(skip=skip, limit=limit)
    return [
        ItemResponse(
            id=str(item.id),
            name=item.name,
            description=item.description
        )
        for item in items
    ]


@router.get(
    "/{item_id}",
    response_model=ItemResponse,
    summary="Obtener item por ID",
    description="Obtiene un item específico por su ID"
)
async def get_item(
    item_id: str = Path(..., description="ID único del item")
) -> ItemResponse:
    item = await item_crud.get_by_id(item_id)
    return ItemResponse(
        id=str(item.id),
        name=item.name,
        description=item.description
    )


@router.put(
    "/{item_id}",
    response_model=ItemResponse,
    summary="Actualizar item",
    description="Actualiza un item existente"
)
async def update_item(
    item_update: ItemUpdate,
    item_id: str = Path(..., description="ID único del item")
) -> ItemResponse:
    updated_item = await item_crud.update(item_id, item_update)
    return ItemResponse(
        id=str(updated_item.id),
        name=updated_item.name,
        description=updated_item.description
    )


@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar item",
    description="Elimina un item de la base de datos"
)
async def delete_item(
    item_id: str = Path(..., description="ID único del item")
) -> None:
    await item_crud.delete(item_id)


@router.get(
    "/stats/count",
    response_model=dict,
    summary="Contar items",
    description="Obtiene el número total de items"
)
async def count_items() -> dict:
    count = await item_crud.count()
    return {"total_items": count}
