from flask import Blueprint, request, jsonify

ingredients = Blueprint("ingredients", __name__, url_prefix="/api/ingredients")

# /api/ingredients/search?q=tom
@ingredients.route("/search", methods=["GET"])
def ingredient_search():
    """

    TODO:  this shoudl have auto-complete, sorted by ingredient popularity  (by default should show most popular ingredients)

    --> if there's a search phrase, the ingredients should be re-ranked by that

    :return:
    """
    query = request.args.get("q", "")
    matches = search_ingredient_names(query)
    return jsonify({"ingredients": matches})
