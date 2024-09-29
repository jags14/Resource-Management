from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from flask_security.models import fsqla_v3 as fsqla
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from .models import db, UserModel

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='username should be a string')
parser.add_argument('email', type=str, required=True, help='email should be a valid string')
parser.add_argument('password', type=str, required=True, help='password should be a string')
parser.add_argument('active', type=bool, required=True, help='username should be a string')
parser.add_argument('fs_uniquifier', type=str, required=True, help='fs_uniquifier should be a string')
parser.add_argument('role_id', type=str, required=True, help='role id should be a string')

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'active': fields.Boolean,
    'fs_uniquifier': fields.String,
    'role_id': fields.String
}

class User(Resource):
    
    def get(self):
        users = db.session.query(UserModel).all()
        users_dict = [user.to_dict() for user in users]
        return users_dict, 200
    
    def post(self):
        args = parser.parse_args()
        user = UserModel(**args)
        db.session.add(user)
        db.session.commit()
        return {"message": "New user created successfully"}, 201
