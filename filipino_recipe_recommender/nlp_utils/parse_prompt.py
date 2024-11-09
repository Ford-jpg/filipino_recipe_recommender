import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Lists with multi-word ingredients and dish types
MULTIWORD_INGREDIENTS = {"pork belly", "soy sauce"}
MULTIWORD_DISH_TYPES = {"fried", "grilled", "stew", "soup", "dessert"}

# Single-word terms for fallback matching
SINGLE_INGREDIENTS = {"chicken", "pork", "beef", "fish", "shrimp", "vinegar", "garlic", "onion"}
SINGLE_DISH_TYPES = {"fried", "grilled", "stew", "soup", "dessert"}
TASTE_PROFILES = {"savory", "sweet", "spicy", "sour"}

def parse_prompt(prompt):
    prompt_lower = prompt.lower()

    # Check for multi-word ingredients and dish types first
    ingredients = {phrase for phrase in MULTIWORD_INGREDIENTS if phrase in prompt_lower}
    dish_types = {phrase for phrase in MULTIWORD_DISH_TYPES if phrase in prompt_lower}
    taste_profiles = set()  # Initialize taste_profiles as an empty set

    # Process the remaining words in the prompt with spaCy
    doc = nlp(prompt_lower)
    
    for token in doc:
        term = token.lemma_
        if term in SINGLE_INGREDIENTS and term not in ingredients:
            ingredients.add(term)
        elif term in SINGLE_DISH_TYPES and term not in dish_types:
            dish_types.add(term)
        elif term in TASTE_PROFILES:
            taste_profiles.add(term)
    
    return {
        "ingredients": list(ingredients),
        "dish_type": list(dish_types),
        "taste_profile": list(taste_profiles)
    }
