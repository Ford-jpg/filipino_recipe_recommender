from models import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    recipes = db.relationship('RecipeIngredient', back_populates='ingredient', cascade="all, delete-orphan")
