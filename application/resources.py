from flask_restful import Resource, Api, reqparse
from .models import db, StudyResourceModel

parser = reqparse.RequestParser()
parser.add_argument('topic', type=str, help='Topic should be a string', required=True)
parser.add_argument('description', type=str, help='Description should be a string', required=True)
parser.add_argument('resource_link', type=str, help='link should be a string', required=True)
class StudyResource(Resource):
    def get(self):
        resources = db.session.query(StudyResourceModel).all()
        resources_dict = [resource.to_dict() for resource in resources]
        return resources_dict, 200
    
    def post(self):
        args = parser.parse_args() # this will give us arguments as a dictionary
        study_resource = StudyResourceModel(**args)
        db.session.add(study_resource)
        db.session.commit()
        return {"message": "Study Resource created successfully"}, 201
