from app import app, db
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from models.tag import Tag
from models.recipe_tag import RecipeTag

with app.app_context():
    db.drop_all()  # Drops all tables
    db.create_all()  # Creates tables as per updated models
    print("Database tables dropped successfully.")
