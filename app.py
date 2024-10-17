from flask import Flask, render_template, url_for
from config import Config
from models import db
from flask_login import LoginManager
from routes.auth import auth_blueprint
from routes.profiles import profiles_blueprint
from routes.jobs import jobs_blueprint

app = Flask(__name__)
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


# Create the database tables if they don't exist yet
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
