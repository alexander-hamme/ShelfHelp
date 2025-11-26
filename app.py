from flask import Flask
from blueprints.ui import ui
from blueprints.api.recipes import recipes
from blueprints.api.ingredients import ingredients
from blueprints.api.images import images

app = Flask(__name__)

# Register blueprints
app.register_blueprint(ui)
app.register_blueprint(recipes)
app.register_blueprint(ingredients)
app.register_blueprint(images)

'''

Auto-Search happens when you are just typing in the search bar - optional phrase, title, etc

once you start filtering by ingredients and/or adding images then you need to click Search

'''

if __name__ == "__main__":
    app.run(debug=True)

