import uuid
from typing import Optional, List
from pydantic import UUID4
from shelfhelp.models.ingredient import Ingredient

ids = [
    uuid.uuid4(),
    uuid.uuid4(),
    uuid.uuid4(),
    uuid.uuid4(),
]

# mock db
MOCK_INGREDIENTS = {
    str(ids[0]): Ingredient(
        id=ids[0],
        name="Garlic",
        popularity=9001,
        description="Pungent and flavorful"
    ),
    str(ids[1]): Ingredient(
        id=ids[1],
        name="Tomato",
        popularity=8500,
        description="A juicy red fruit used as a vegetable"
    ),
    str(ids[2]): Ingredient(
        id=ids[2],
        name="Onion",
        popularity=7200,
        description="onion ownyun"
    ),
    str(ids[3]): Ingredient(
        id=ids[3],
        name="Olive Oil",
        popularity=6500,
        description="oily goodness"
    ),
}

async def get_by_id(ingred_id: UUID4) -> Optional[Ingredient]:
    return MOCK_INGREDIENTS.get(str(ingred_id))


async def autocomplete_ingredients(q: str) -> List[Ingredient]:
    if not q:
        # Default = most popular ingredients
        return sorted(MOCK_INGREDIENTS.values(), key=lambda x: -x.popularity)

    # Simple name matching. Replace w/ trigram, BM25, embedding search, etc.
    matches = [
        ing for ing in MOCK_INGREDIENTS.values()
        if q.lower() in ing.name.lower()
    ]

    # Optionally re-rank by search relevance AND popularity
    return sorted(matches, key=lambda x: (-x.popularity, x.name))
