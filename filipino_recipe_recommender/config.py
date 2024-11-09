import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/filipino_recipe_recommender'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
