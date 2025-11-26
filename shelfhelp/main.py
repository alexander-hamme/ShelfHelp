from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import recipes, ingredients, images

app = FastAPI(title="Recipe Assistant API")

# Static + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routers
app.include_router(recipes.router, prefix="/api/recipes", tags=["recipes"])
app.include_router(ingredients.router, prefix="/api/ingredients", tags=["ingredients"])
app.include_router(images.router, prefix="/api/images", tags=["images"])


@app.get("/", include_in_schema=False)
async def index(request):
    return templates.TemplateResponse("index.html", {"request": request})
