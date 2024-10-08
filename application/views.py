from flask import current_app as app
from flask_security import auth_required, roles_required

@app.get('/')
def home():
    return 'Hello World'

@app.get('/admin')
@auth_required('token')
@roles_required('admin')
def admin():
    return "welcome, admin"