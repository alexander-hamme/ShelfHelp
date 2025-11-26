from fastapi import APIRouter, Depends, Query
from pydantic import UUID4

from shelfhelp.models.ingredient import Ingredient, IngredientMatch
from shelfhelp.dependencies.ingredients import valid_ingredient_id
from shelfhelp.services.ingredients_service import autocomplete_ingredients

router = APIRouter()


# GET /api/ingredients/{ingred_id}
@router.get("/{ingred_id}", response_model=Ingredient)
async def get_ingredient_by_id(
    ingredient: Ingredient = Depends(valid_ingredient_id)
):
    return ingredient


# GET /api/ingredients/{ingred_id}/related
@router.get("/{ingred_id}/related", response_model=list[IngredientMatch])
async def get_related_ingredients(
    ingredient: Ingredient = Depends(valid_ingredient_id),
):
    """
    TODO:  once you've selected one ingredient, these will show up as the next options when the search is cleared
    :param ingredient:
    :return:
    """

    # Stub logic — replace with real related-ingredient logic
    return [
        IngredientMatch(
            id=ingredient.id,
            name=ingredient.name,
            popularity=ingredient.popularity,
            confidence=1.0
        )
    ]


# GET /api/ingredients/search?q=garlic
@router.get("/search", response_model=list[IngredientMatch])
async def ingredient_search(
    q: str = Query("", description="Ingredient name"),
):
    """

       TODO:  this shoudl have auto-complete, sorted by ingredient popularity  (by default should show most popular ingredients)

       --> if there's a search phrase, the ingredients should be re-ranked by that

       :return:
       """

    """
    Ingredient autocomplete search.

    Behavior:
    - If `q` is empty → returns most popular ingredients
    - If `q` has text → autocomplete + re-ranked by popularity
    """
    results = await autocomplete_ingredients(q)

    # Convert Ingredient → IngredientMatch
    return [
        IngredientMatch(
            id=ing.id,
            name=ing.name,
            popularity=ing.popularity,
            confidence=None,
        )
        for ing in results
    ]


