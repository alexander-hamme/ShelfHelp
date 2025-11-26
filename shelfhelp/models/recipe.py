from shelfhelp.models import CustomModel

class RecipeResult(CustomModel):
    title: str
    description: str
    author: str | None = None
    keywords: list[str] = []

class IngredientRequest(CustomModel):
    ingredients: list[str]
