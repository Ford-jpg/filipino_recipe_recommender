from flask import Flask, jsonify, g, request
import time
from config import Config
from models import db  # Import only db here
from routes.recipe_routes import recipe_routes  # Import the recipe routes Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db.init_app(app)

# Register the Blueprint for recipe routes
app.register_blueprint(recipe_routes, url_prefix='/api')

# Root route to handle requests to "/"
@app.route('/')
def index():
    return "Welcome to the API"

# Performance monitoring
@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    print(f"Request to {request.path} took {duration:.4f} seconds")
    return response

# Basic health check route
@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

if __name__ == '__main__':
    # Initialize database tables if they don't exist
    with app.app_context():
        db.create_all()  # Create tables in the database
    app.run(debug=False)
