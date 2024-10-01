from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
# from database import Base

db = SQLAlchemy()

# secondary table for mamy-to-many relationship between users and roles
class RolesUsers(db.Model):
    # __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))

class UserModel(db.Model, UserMixin):
    # __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True)
    roles = db.relationship('RoleModel', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    # study_resource = db.relationship('StudyResource', backref='creator')

    # def __init__(self, username, email, password, active, fs_uniquifier, roles):

    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.active = active
    #     self.fs_uniquifier = fs_uniquifier
    #     self.roles = roles
    
    # def to_dict(self):
    #     return {
    #         'username': self.username,
    #         'email': self.email,
    #         'active': self.active,
    #         'fs_uniquifier': self.fs_uniquifier,
    #         'role_id': self.role_id,
    #         'role': self.role
    #     }

class RoleModel(db.Model, RoleMixin):
    # __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description

class StudyResourceModel(db.Model):
    # __tablename__ = 'resources'
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
    
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'topic': self.topic,
    #         'description': self.description,
    #         'resource_link': self.resource_link,
    #         'is_approved': self.is_approved
    #     }