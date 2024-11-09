import pandas as pd
from app import app, db
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

# Path to your CSV file
DATA_CSV = r"C:\Users\User\Desktop\Recommender\recipes.csv"

def load_data():
    data_df = pd.read_csv(DATA_CSV, encoding='latin1')
    
    existing_recipes = set()
    existing_ingredients = {}

    for _, row in data_df.iterrows():
        recipe_id = row['recipe_id']
        title = row['title']
        description = row['description']
        instructions = row['instructions']
        dish_type = row['dish_type']
        taste_profile = row['taste_profile']
        keywords_text = row['keyword']  # Use renamed column 'keyword' from CSV

        # Load Recipe with keyword column populated
        if recipe_id not in existing_recipes:
            recipe = Recipe(
                recipe_id=recipe_id,
                title=title,
                description=description,
                instructions=instructions,
                dish_type=dish_type,
                taste_profile=taste_profile,
                keyword=keywords_text  # Save keywords in the Recipe model
            )
            db.session.add(recipe)
            db.session.flush()  # Ensure recipe ID is available for relationships
            existing_recipes.add(recipe_id)

        # Process and Load each keyword as an Ingredient
        keywords_list = [keyword.strip() for keyword in keywords_text.split(',')]
        for keyword in keywords_list:
            # Check if ingredient already exists in the database
            if keyword not in existing_ingredients:
                ingredient = Ingredient(name=keyword)
                db.session.add(ingredient)
                db.session.flush()  # Get ingredient_id for linking
                existing_ingredients[keyword] = ingredient.ingredient_id

            # Link Recipe and Ingredient with RecipeIngredient
            recipe_ingredient = RecipeIngredient(
                recipe_id=recipe.recipe_id,
                ingredient_id=existing_ingredients[keyword],
                quantity="",  # Quantity and unit not provided in this CSV
                unit=""
            )
            db.session.add(recipe_ingredient)

    db.session.commit()
    print("Data loaded successfully from the CSV file.")

if __name__ == "__main__":
    with app.app_context():
        load_data()
