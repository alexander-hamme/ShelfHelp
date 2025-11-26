from shelfhelp.models import CustomModel
from pydantic import UUID4
from typing import Optional

class IngredientMatch(CustomModel):
    id: UUID4
    name: str
    popularity: int
    confidence: Optional[float] = None

class Ingredient(CustomModel):
    id: UUID4
    name: str
    popularity: int
    description: Optional[str] = None