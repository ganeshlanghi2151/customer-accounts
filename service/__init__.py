
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Configure the application's existing settings here.
    CORS(app)
    Talisman(app)

    return app
