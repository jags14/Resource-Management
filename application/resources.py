from flask_restful import Resource, Api
# api = Api()

class StudyResource(Resource):
    def get(self):
        return {"message": "hello from api"}
