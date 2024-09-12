from flask import Flask
from database import db_session

# create_app function is an app-factory method of creating flask apps
def create_app():
    app = Flask(__name__)
    with app.app_context():
        import application.views
    return app

app = create_app()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)