import asyncio

from fastapi import APIRouter, Query
from shelfhelp.models.recipe import RecipeResult, IngredientRequest

router = APIRouter()

@router.get("/search", response_model=list[RecipeResult])
async def search_recipes(
    query: str = Query("", description="search phrase"),
    mode: str = Query("title", regex="^(title|description|keywords|author|all)$")
):
    # match mode:
    #     case "title":
    #         pass
    #     case "author":
    #         pass
    return await search_recipe_db(query,  mode)


async def search_recipe_db(query, search_mode):

    # raise specific errors here and/or perform logic

    await asyncio.sleep(1)

    # This is the placeholder dictionary that is returned

    return [
        RecipeResult(title="Shit-Caked Ass", description="A blorious backshotted bubble bass bouncing in shit",
                     author="Nigward Testicles", keywords=[])
    ]
    # if search_mode not in MY_CLASS.SEARCH_MODES:

    if results is None:
        return jsonify({"error": "unknown search type"}), 400

    return jsonify({"results": results})


@router.post("/from-ingredients", response_model=list[RecipeResult])
async def search_from_ingredients(req: IngredientRequest):
    return await recipe_match_by_ingredients(req.ingredients)