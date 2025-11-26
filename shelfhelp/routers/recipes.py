from fastapi import APIRouter, Query
from models.recipe import RecipeResult, IngredientRequest

router = APIRouter()

@router.get("/search", response_model=list[RecipeResult])

@recipes.route("/search", methods=["GET"])
def search_recipes():
    query = request.args.get("q", "")
    search_mode = request.args.get("type", "title")  # default = title search

    # match mode:
    #     case "title":
    #         pass
    #     case "author":
    #         pass
    results = search_recipe_db(query, search_mode)

    # if search_mode not in MY_CLASS.SEARCH_MODES:

    if results is None:
        return jsonify({"error": "unknown search type"}), 400

    return jsonify({"results": results})

@recipes.route("/recipe", methods=["GET"])
def get_recipe():
    recipe_id = request.args.get("id")
    # TODO flask auto-input validation / type parsing ?
    if recipe_id is None:
        return jsonify({"error": "missing recipe id"}), 400
    elif recipe_id not in recipes:
        return jsonify({"error": "recipe id not found"}), 404
    else:
        return None # render_template("recipe") --> dynamically generated full page recipe view

def search_recipe_db(query, search_mode):

    # raise specific errors here and/or perform logic

    return {}