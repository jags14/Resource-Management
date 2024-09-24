from main import app
from application.models import db, Role

with app.app_context():
    # this code will have access to application level data
    db.create_all()
    # creates all tables in the database

    admin = Role(id='admin', name='Admin', description='admin description')
    db.session.add(admin)
    student = Role(id='student', name='Student', description='student description')
    db.session.add(student)
    instructor = Role(id='instructor', name='Instructor', description='Instructor description')
    db.session.add(instructor)

    db.session.commit()


