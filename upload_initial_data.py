from main import app, datastore
from application.models import db, RoleModel
from flask_security import hash_password

with app.app_context():
    # this code will have access to application level data
    db.create_all()

    datastore.find_or_create_role(name='admin', description='User is the admin')
    datastore.find_or_create_role(name='inst', description='User is an instructor')
    datastore.find_or_create_role(name='stud', description='User is an Student')
    db.session.commit()

    if not datastore.find_user(email='admin@gmail.com'):
        datastore.create_user(username='adminuser', email='admin@gmail.com', password=hash_password("admin"), roles=['admin'])
        db.session.commit()
    if not datastore.find_user(email='instruct1@gmail.com'):
        datastore.create_user(username='instructoruser', email='instruct1@gmail.com', password=hash_password("instruct1"), roles=['inst'])
        db.session.commit()
    if not datastore.find_user(email='student1@gmail.com'):
        datastore.create_user(username='studentuser', email='student1@gmail.com', password=hash_password("student1"), roles=['stud'])
        db.session.commit()
    
        

