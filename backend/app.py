from venv import create
from create_app import create_app, session
from database.models import db, User
from flask_cors import CORS
from flask_jwt_extended import create_access_token

app = create_app()
CORS(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.run(host="192.168.0.101", port=5050)
