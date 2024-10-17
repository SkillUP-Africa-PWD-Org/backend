from app import app, db
from models import Curriculum, Lesson

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Dummy Curriculum and Lessons
    curriculum1 = Curriculum(course_title="Introduction to Python", course_description="Learn the basics of Python programming.")
    lesson1 = Lesson(lesson="Python Basics", content="Introduction to Python blah blah", images=None, curriculum=curriculum1)
    lesson2 = Lesson(lesson="Data Science Introduction", content="Data Science 101", images=None, curriculum=curriculum1)
    lesson3 = Lesson(lesson="Web Development with Flask", content="Learn how to build web applications using Flask.", images=None, curriculum=curriculum1)

    curriculum2 = Curriculum(course_title="Advanced Python", course_description="Learn advanced Python programming concepts.")
    lesson4 = Lesson(lesson="Decorators and Generators", content="Understanding advanced Python features.", images=None, curriculum=curriculum2)

    # Add all to session and commit
    db.session.add_all([curriculum1, lesson1, lesson2, lesson3, curriculum2, lesson4])
    db.session.commit()

    print("Dummy data with lessons inserted successfully!")
