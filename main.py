from flask import Flask
from application.models import db
from config import DevelopmentConfig
from application.resources import StudyResource
from flask_restful import Api

# create_app function is an app-factory method of creating flask apps
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    api = Api(app)
    api.add_resource(StudyResource, '/study')
    
    with app.app_context():
        import application.views
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)