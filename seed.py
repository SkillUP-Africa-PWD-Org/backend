from app import app, db
from models import Curriculum, Lesson

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Dummy Curriculum and Lessons

    # Curriculum 1: Mechanics
    curriculum_mechanics = Curriculum(course_title="Introduction to Mechanics", course_description="Learn the basics of Mechanics.")
    lesson_mechanics_1 = Lesson(lesson="Mechanics 101", content="Mechanics course 1.pdf", images=None, curriculum=curriculum_mechanics)
    lesson_mechanics_2 = Lesson(lesson="Mechanics 102", content="Mechanics course 2.pdf", images=None, curriculum=curriculum_mechanics)

    # Curriculum 2: Plumbing
    curriculum_plumbing = Curriculum(course_title="Introduction to Plumbing", course_description="Learn the basics of Plumbing.")
    lesson_plumbing_1 = Lesson(lesson="Plumbing 101", content="Plumbing course 1.pdf", images=None, curriculum=curriculum_plumbing)

    # Curriculum 3: Advanced Python
    curriculum_python = Curriculum(course_title="Advanced Python", course_description="Learn advanced Python programming concepts.")
    lesson_python_1 = Lesson(lesson="Decorators and Generators", content="Understanding advanced Python features.", images=None, curriculum=curriculum_python)

    # Add all to session and commit
    db.session.add_all([curriculum_mechanics, lesson_mechanics_1, lesson_mechanics_2,
                        curriculum_plumbing, lesson_plumbing_1,
                        curriculum_python, lesson_python_1])
    
    db.session.commit()

    print("Dummy data with lessons inserted successfully!")
