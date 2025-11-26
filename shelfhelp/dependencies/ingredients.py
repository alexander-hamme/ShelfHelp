from fastapi import Depends
from pydantic import UUID4
from typing import Any
from shelfhelp.services.ingredients_service import get_by_id
from fastapi import HTTPException, status

class IngredientNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingredient not found",
        )

async def valid_ingredient_id(ingred_id: UUID4) -> Any:
    ingredient = await get_by_id(ingred_id)
    if not ingredient:
        raise IngredientNotFound()
    return ingredient
