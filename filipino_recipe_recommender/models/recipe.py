from models import db
from .recipe_ingredient import RecipeIngredient
from .tag import Tag
from sqlalchemy import Column, Integer, String, Text

class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    instructions = db.Column(db.Text)
    dish_type = db.Column(db.String(50))
    taste_profile = db.Column(db.String(50))
    keyword = Column(Text, nullable=True)

    ingredients = db.relationship('RecipeIngredient', back_populates='recipe', cascade="all, delete-orphan")
    tags = db.relationship('Tag', secondary='recipe_tags', back_populates='recipes')
