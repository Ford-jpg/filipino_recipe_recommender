from flask import Blueprint, jsonify, request
from models import db
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from sqlalchemy import func, or_
from nlp_utils.parse_prompt import parse_prompt

recipe_routes = Blueprint('recipe_routes', __name__)

@recipe_routes.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipes = Recipe.query.limit(5).all()
    return jsonify([{"title": recipe.title, "description": recipe.description} for recipe in recipes])

@recipe_routes.route('/recipes/prompt_search', methods=['POST'])
def prompt_search():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "Please provide a search prompt"}), 400

    # Parse the prompt to extract potential keywords, dish type, and taste profile
    parsed_terms = parse_prompt(prompt)
    ingredients = [ing.lower() for ing in parsed_terms["ingredients"]]
    dish_type = parsed_terms["dish_type"]
    taste_profile = parsed_terms["taste_profile"]

    # Build the query based on parsed terms
    query = Recipe.query
    if ingredients:
        # Search in `keyword` field in Recipe model to find ingredients match
        ingredient_filters = [func.lower(Recipe.keyword).ilike(f"%{ing}%") for ing in ingredients]
        query = query.filter(or_(*ingredient_filters))
    if dish_type:
        query = query.filter(func.lower(Recipe.dish_type).in_([dt.lower() for dt in dish_type]))
    if taste_profile:
        query = query.filter(func.lower(Recipe.taste_profile).in_([tp.lower() for tp in taste_profile]))

    # Limit results to 5 and fetch
    recipes = query.limit(5).all()

    # Format the response with title and description
    results = [{"recipe_id": recipe.recipe_id, "title": recipe.title, "description": recipe.description} for recipe in recipes]
    return jsonify(results)
