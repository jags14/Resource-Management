
from flask_sqlalchemy import SQLAlchemy
# from database import Base

db = SQLAlchemy(session_options='scoped_session')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    role_id = db.Column(db.String, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    role = db.relationship('Role')
    study_resource = db.relationship('resources', backref='creator')
    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

class StudyResource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    resource_link = db.Column(db.String, nullable=False)
    is_approved = db.Column(db.Boolean(), default=False)

