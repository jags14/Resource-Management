from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
# from database import Base

db = SQLAlchemy()

# secondary table for mamy-to-many relationship between users and roles
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True)
    roles = db.relationship('RoleModel', secondary='roles_users', back_populates='users')
   
class RoleModel(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    users = db.relationship('UserModel', secondary='roles_users', back_populates='roles')


class StudyResourceModel(db.Model):
    __tablename__ = 'resource'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    # creator = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    resource_link = db.Column(db.String(), nullable=False)
    is_approved = db.Column(db.Boolean(), default=False)

    def __init__(self, topic, description, resource_link, is_approved=False):
        self.topic = topic
        self.description = description
        self.resource_link = resource_link
        self.is_approved = is_approved
    