from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    profile_pic_url = db.Column(db.String(500), nullable=True)

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String(100), nullable=False)
    course_description = db.Column(db.Text, nullable=False)
    # A course can have multiple lessons

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column(db.String(200), nullable=False)  # Lesson title
    content = db.Column(db.Text, nullable=False)  # Lesson content
    images = db.Column(db.String(500), nullable=True)  # Optional images URL or description
    curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculum.id'), nullable=False)  # Foreign key to Curriculum

    curriculum = db.relationship('Curriculum', backref=db.backref('lessons', lazy=True))