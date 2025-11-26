from fastapi import APIRouter, Query
from models.ingredient import IngredientMatch

router = APIRouter()

@router.get("/search", response_model=list[IngredientMatch])
async def ingredient_search(
    q: str = Query("", description="Ingredient name")
):
    """

    TODO:  this shoudl have auto-complete, sorted by ingredient popularity  (by default should show most popular ingredients)

    --> if there's a search phrase, the ingredients should be re-ranked by that

    :return:
    """
    return await autocomplete_ingredients(q)