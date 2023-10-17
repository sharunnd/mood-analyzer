from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app instance
template_dir = os.path.abspath('templates')

# Initialize Flask app instance with static URL path
app = Flask(__name__, static_url_path='/mood_analyzer/static', template_folder=template_dir)


# Configure Flask app with MongoDB URI from environment variables
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Secret key for Flask sessions

# Initialize MongoDB connection
mongo = PyMongo(app)

# Import and register the blueprint(s)
from app.routes import dashboard_bp
app.register_blueprint(dashboard_bp, url_prefix='/')
