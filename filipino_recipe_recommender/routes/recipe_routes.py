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
    recipes = Recipe.query.limit(5).all()  # Limit results to 5
    return jsonify([{"title": recipe.title, "description": recipe.description} for recipe in recipes])

@recipe_routes.route('/recipes/search', methods=['POST'])
def search_recipes():
    data = request.get_json()
    input_ingredients = data.get('ingredients', [])

    if not input_ingredients:
        return jsonify({"error": "Please provide a list of ingredients for search"}), 400

    # Using `func.ilike` with `or_` to match substrings in ingredients for better flexibility
    ingredient_filters = [func.lower(Ingredient.name).ilike(f"%{ing.lower()}%") for ing in input_ingredients]
    
    matching_recipes = db.session.query(Recipe).join(RecipeIngredient).join(Ingredient).filter(or_(*ingredient_filters)).distinct().limit(5).all()

    # Format the response
    results = [{"recipe_id": recipe.recipe_id, "title": recipe.title, "description": recipe.description} for recipe in matching_recipes]
    return jsonify(results)

@recipe_routes.route('/recipes/prompt_search', methods=['POST'])
def prompt_search():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "Please provide a search prompt"}), 400

    # Parse the prompt to extract ingredients, dish type, and taste profile
    parsed_terms = parse_prompt(prompt)
    ingredients = [ing.lower() for ing in parsed_terms["ingredients"]]  # Ensure case-insensitive search
    dish_type = parsed_terms["dish_type"]
    taste_profile = parsed_terms["taste_profile"]

    # Build SQL query based on parsed terms
    query = Recipe.query
    if ingredients:
        ingredient_filters = [func.lower(Ingredient.name).ilike(f"%{ing}%") for ing in ingredients]
        query = query.join(RecipeIngredient).join(Ingredient).filter(or_(*ingredient_filters))
    if dish_type:
        query = query.filter(func.lower(Recipe.dish_type).in_([dt.lower() for dt in dish_type]))
    if taste_profile:
        query = query.filter(func.lower(Recipe.taste_profile).in_([tp.lower() for tp in taste_profile]))

    # Limit results to 5
    recipes = query.limit(5).all()

    # Format the response
    results = [{"recipe_id": recipe.recipe_id, "title": recipe.title, "description": recipe.description} for recipe in recipes]
    return jsonify(results)

@recipe_routes.route('/recipes/keyword_search', methods=['POST'])
def keyword_search():
    data = request.get_json()
    input_keywords = data.get("keywords", [])

    if not input_keywords:
        return jsonify({"error": "No keywords provided for search"}), 400

    # Using `ilike` for flexible keyword-based search
    keyword_filters = [Recipe.keyword.ilike(f"%{keyword}%") for keyword in input_keywords]
    recipes = Recipe.query.filter(or_(*keyword_filters)).limit(5).all()

    # Format results to JSON
    results = [{"title": recipe.title, "description": recipe.description} for recipe in recipes]
    return jsonify(results)
