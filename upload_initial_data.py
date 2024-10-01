from main import app, datastore
from application.models import db, RoleModel
from flask_security import UserDatastore

with app.app_context():
    # this code will have access to application level data
    db.create_all()
    # creates all tables in the database
    # admin = RoleModel(id='admin', name='Admin', description='admin description')
    # db.session.add(admin)
    # student = RoleModel(id='student', name='Student', description='student description')
    # db.session.add(student)
    # instructor = RoleModel(id='instructor', name='Instructor', description='Instructor description')
    # db.session.add(instructor)
    # db.session.commit()
    datastore.find_or_create_role(name='admin', description='User is the admin')
    datastore.find_or_create_role(name='inst', description='User is an instructor', active=False)
    datastore.find_or_create_role(name='stud', description='User is an Student')
    db.session.commit()

    if not datastore.find_user(email='admin@gmail.com'):
        datastore.create_user(email='admin@gmail.com', password='admin', roles=['admin'])
    if not datastore.find_user(email='instruct1@gmail.com'):
        datastore.create_user(email='instruct1@gmail.com', password='instruct1', roles=['inst'])
    if not datastore.find_user(email='student1@gmail.com'):
        datastore.create_user(email='student1@gmail.com', password='student1', roles=['stud'])


