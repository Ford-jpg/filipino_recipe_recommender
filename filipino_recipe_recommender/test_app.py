from app import app, db
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from sqlalchemy import func

with app.app_context():
    # Check for recipes containing specific ingredients
    ingredient = "soy sauce"  # Lowercase for consistency
    recipes = db.session.query(Recipe).join(RecipeIngredient).join(Ingredient).filter(
        func.lower(Ingredient.name) == ingredient.lower()
    ).all()
    
    print(f"Found {len(recipes)} recipes for '{ingredient}'")
    for recipe in recipes:
        print(recipe.title)
