from flask import Flask


app = Flask(__name__)


def created_app(enviroment):
    app.config.from_object(enviroment)
    return app