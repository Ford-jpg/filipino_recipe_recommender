# Filipino Recipe Recommender API Roadmap

This roadmap outlines the steps to complete the Filipino Recipe Recommender API using Flask for the backend and PostgreSQL as the database.

---

## Phase 1: Project Setup

### 1.1 Environment Setup
- [ ] **Install Dependencies**: Set up a virtual environment and install Flask, Psycopg2 (for PostgreSQL), SQLAlchemy (optional ORM), and other essential libraries.
- [ ] **Initialize Git Repository**: Set up version control for the project.
- [ ] **Create Configuration Files**:
  - `config.py`: For storing environment variables and database configurations.
  - `.env`: For secure handling of sensitive data (like database credentials).

### 1.2 Database Setup
- [ ] **Define Database Schema**: Outline tables and relationships.
  - **Recipes Table**: Fields for `recipe_id`, `title`, `ingredients`, `instructions`, `taste_profile`, `dish_type`, etc.
  - **Ingredients Table**: Fields for `ingredient_id`, `name`.
  - **Tags Table**: (Optional) Fields for taste tags like `spicy`, `sweet`, etc.
  - **Recipe_Ingredients Table**: For many-to-many relationships between recipes and ingredients.
- [ ] **Create Database**: Use PostgreSQL to create the database named `filipino_recipe_recommender`.
- [ ] **Migrations**: Use Alembic or Flask-Migrate to handle database migrations.

---

## Phase 2: API Development

### 2.1 Basic API Structure
- [ ] **Create Flask App**: Initialize the Flask application.
- [ ] **Define Routes**:
  - `GET /recipes`: For searching and filtering recipes.
  - `POST /recipes/search`: For advanced searches with ingredients and prompts.

### 2.2 Ingredient-Based Search
- [ ] **Route Logic** (`POST /recipes/search`):
  - Parse the input for a list of ingredients.
  - Construct SQL query to find recipes that match the ingredients.
  - Apply a threshold filter (e.g., minimum 60% ingredient match).
  - Return results sorted by match percentage.

### 2.3 Prompt-Based Search
- [ ] **Natural Language Processing**: Integrate NLP for parsing user prompts.
  - Use libraries like spaCy or NLTK for prompt analysis.
  - Extract key terms (e.g., main ingredient, dish type, taste descriptors).
- [ ] **SQL Query Construction**:
  - Use parsed terms to search for recipes matching ingredients, dish type, or taste profile.
  - Return results based on a relevance score.

---

## Phase 3: Scoring System

### 3.1 Define Scoring Algorithm
- [ ] **Scoring Criteria**:
  - Ingredient Match Score
  - Keyword Match Score
  - Relevance Score (using NLP similarity if possible)
- [ ] **SQL Integration**:
  - Adjust SQL queries to include scoring calculations.
  - Return sorted recipes based on the calculated `total_score`.

### 3.2 Testing and Refinement
- [ ] **Testing with Sample Inputs**: Try various ingredient lists and prompts.
- [ ] **Adjust Thresholds**: Fine-tune thresholds for ingredient match percentages and relevance.

---

## Phase 4: Data Population and Optimization

### 4.1 Data Entry
- [ ] **Recipe Data**: Populate the database with Filipino recipes.
- [ ] **Ingredient List**: Ensure that ingredients are consistently named to avoid duplicate entries.

### 4.2 Query Optimization
- [ ] **Indexing**: Add indexes on frequently searched columns (e.g., `title`, `ingredients`).
- [ ] **Performance Testing**: Measure query response times and optimize where needed.

---

## Phase 5: Finalization and Deployment

### 5.1 API Documentation
- [ ] **Document Endpoints**: Use Swagger or Postman to document each endpoint.
- [ ] **Write Usage Examples**: Include examples for both ingredient-based and prompt-based searches.

### 5.2 User Feedback System (Optional)
- [ ] **Feedback Endpoint**: Create an endpoint where users can rate the recommended recipes.
- [ ] **Feedback Storage**: Store ratings in the database to analyze user satisfaction.

### 5.3 Deployment
- [ ] **Deploy API**: Use a platform like Heroku, DigitalOcean, or AWS for deployment.
- [ ] **Set Up Environment Variables**: Ensure sensitive information like database credentials is securely stored.
- [ ] **Test in Production**: Perform end-to-end testing on the live API.

---

## Future Improvements

- **Enhance NLP Parsing**: Integrate more advanced NLP techniques for improved prompt interpretation.
- **Add User Accounts**: Allow users to save recipes and preferences.
- **Machine Learning for Personalization**: Use ML to personalize recommendations based on user history.

---

This roadmap will guide us step-by-step to completion.
