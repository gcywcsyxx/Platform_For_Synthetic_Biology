from flask import Flask
from . import routes

def create_app(config_name="default"):
    app = Flask(__name__)
    routes.init_app(app)

    return app