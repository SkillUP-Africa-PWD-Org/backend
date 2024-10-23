from flasgger import Swagger
from flask import Flask, jsonify
from config import Config
from models import db, User
from flask_login import LoginManager
from routes.auth import auth_blueprint
from routes.profiles import profiles_blueprint
from routes.jobs import jobs_blueprint
from routes.curriculum import curriculum_blueprint

# Initialize Flask and Flasgger
app = Flask(__name__)
swagger = Swagger(app)  # Flasgger automatically sets up Swagger UI

app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Register Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(profiles_blueprint)
app.register_blueprint(jobs_blueprint)
app.register_blueprint(curriculum_blueprint)


# Define the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load the user from the database by their ID

# Add a simple route for the homepage
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the SkillUP Application API!"})

# Create the database tables if they don't exist yet
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
