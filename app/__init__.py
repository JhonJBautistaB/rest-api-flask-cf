from flask import Flask
from .models import db


app = Flask(__name__)


def created_app(enviroment):
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app