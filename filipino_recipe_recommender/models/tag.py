from models import db

class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), unique=True, nullable=False)

    recipes = db.relationship('Recipe', secondary='recipe_tags', back_populates='tags')
