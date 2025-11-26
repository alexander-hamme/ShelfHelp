import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from shelfhelp.routers import recipes, ingredients, images


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app = FastAPI(title="Shelf Help Recipe Assistant API")

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Routers
app.include_router(recipes.router, prefix="/api/recipes", tags=["recipes"])
app.include_router(ingredients.router, prefix="/api/ingredients", tags=["ingredients"])
app.include_router(images.router, prefix="/api/images", tags=["images"])


@app.get("/", include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
