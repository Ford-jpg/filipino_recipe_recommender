import spacy
from googletrans import Translator

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# All keywords as single phrases to enable partial matching
ALL_KEYWORDS = {
    "pork belly",
    "soy sauce",
    "vinegar",
    "garlic",
    "bay leaves",
    "peppercorns",
    "sugar",
    "water",
    "salt",
    "pork spare ribs",
    "tamarind pulp",
    "tomatoes",
    "onion",
    "radish",
    "string beans",
    "eggplant",
    "kangkong leaves",
    "green chili",
    "oxtail",
    "peanut butter",
    "annatto seeds",
    "banana heart",
    "bok choy",
    "shrimp paste",
    "oil",
    "chicken",
    "green papaya",
    "ginger",
    "malunggay leaves",
    "fish sauce",
    "pancit canton noodles",
    "shrimp",
    "carrot",
    "cabbage",
    "bell pepper",
    "snow peas",
    "oyster sauce",
    "beef shank",
    "corn on the cob",
    "coconut milk",
    "coconut cream",
    "red chili",
    "calamansi juice",
    "pepper",
    "dried taro leaves",
    "liver spread",
    "potatoes",
    "carrots",
    "green peas",
    "olives",
    "pork hock",
    "banana blossoms",
    "brown sugar",
    "squash",
    "bitter melon",
    "okra",
    "glutinous rice",
    "green onions",
    "ground pork",
    "spring roll wrapper",
    "pork lungs",
    "chili",
    "pork cheeks",
    "mayonnaise",
    "mung beans",
    "spinach leaves",
    "annatto oil",
    "sausage casing",
    "pork leg",
    "beef tapa",
    "fried eggs",
    "garlic fried rice",
    "pork blood",
    "pork intestines",
    "rice flour",
    "lye water",
    "grated coconut",
    "baking powder",
    "banana leaves",
    "salted egg slices",
    "cocoa powder",
    "evaporated milk",
    "ube",
    "condensed milk",
    "butter",
    "food coloring",
    "coconut curds",
    "saba bananas",
    "lumpia wrappers",
    "jackfruit",
    "young coconut",
    "flour",
    "cornstarch",
    "shaved ice",
    "milk",
    "sweetened beans",
    "assorted jellies",
    "nata de coco",
    "dough for crust",
    "all-purpose flour",
    "yeast",
    "egg",
    "beef sirloin",
    "sugar for caramel",
    "rice noodles",
    "shrimp broth",
    "crushed chicharon",
    "calamansi",
    "egg noodles",
    "camote",
    "winged beans",
    "bagoong",
    "taro leaves",
    "cabbage",
    "green beans",
}


# Sets for dish types and taste profiles as used previously
DISH_TYPES = {"fried", "grilled", "stew", "soup", "dessert"}
TASTE_PROFILES = {"savory", "sweet", "spicy", "sour"}

def parse_prompt(prompt):
    translator = Translator()
    
    # Detect and translate if necessary
    detected_lang = translator.detect(prompt).lang
    if detected_lang in ["ceb", "tl"]:  # Cebuano or Filipino
        prompt = translator.translate(prompt, dest='en').text
    
    prompt_lower = prompt.lower()

    # Find keywords, dish types, and taste profiles within the prompt
    matched_keywords = {kw for kw in ALL_KEYWORDS if kw in prompt_lower}
    matched_dish_types = {dt for dt in DISH_TYPES if dt in prompt_lower}
    matched_taste_profiles = {tp for tp in TASTE_PROFILES if tp in prompt_lower}
    
    # Parse remaining single words in the prompt
    doc = nlp(prompt_lower)
    for token in doc:
        term = token.lemma_
        # Add terms not already captured by keywords or dish types
        if term in DISH_TYPES and term not in matched_dish_types:
            matched_dish_types.add(term)
        elif term in TASTE_PROFILES and term not in matched_taste_profiles:
            matched_taste_profiles.add(term)

    return {
        "ingredients": list(matched_keywords),
        "dish_type": list(matched_dish_types),
        "taste_profile": list(matched_taste_profiles)
    }
