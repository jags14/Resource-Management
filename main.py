import os
from dotenv import load_dotenv
from flask import Flask
from application.models import db
from config import DevelopmentConfig
from application.resources import StudyResource
from flask_restful import Api
from flask_security import Security, SQLAlchemyUserDatastore,auth_required, hash_password
from application.users import User

load_dotenv()
# create_app function is an app-factory method of creating flask apps
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")
    api = Api(app)
    api.add_resource(StudyResource, '/study')
    api.add_resource(User, '/users')
    
    with app.app_context():
        import application.views
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)