from app import app, db
from models import Curriculum, Lesson

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Dummy Curriculum and Lessons

    # Curriculum 1: Plumbing
    curriculum_plumbing = Curriculum(course_title="Introduction to Plumbing", course_description="Learn the basics of Plumbing.")
    lesson_plumbing_1 = Lesson(lesson="Plumbing 101", content="Plumbing course 1.pdf", images=None, curriculum=curriculum_plumbing)

    # Curriculum 2: Tailoring
    curriculum_tailoring = Curriculum(course_title="Tailoring", course_description="Create, Customize and master tailoring.")
    lesson_tailoring_1 = Lesson(lesson="Tailoring 101", content="Tailoring course 1.pdf", images=None, curriculum=curriculum_tailoring)

    # Add all to session and commit
    db.session.add_all([curriculum_plumbing, lesson_plumbing_1,
                        curriculum_tailoring, lesson_tailoring_1])
    
    db.session.commit()

    print("Dummy data with lessons inserted successfully!")
