from app import app, db
from models.recipe import Recipe

with app.app_context():
    recipes = Recipe.query.all()
    print(f"Found {len(recipes)} recipes in the database.")
    for recipe in recipes:
        print(f"Title: {recipe.title}, Description: {recipe.description}")
