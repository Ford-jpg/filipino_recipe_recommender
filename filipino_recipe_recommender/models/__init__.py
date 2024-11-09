from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models for database table registration
from .recipe import Recipe
from .ingredient import Ingredient
from .recipe_ingredient import RecipeIngredient
from .tag import Tag
from .recipe_tag import RecipeTag
