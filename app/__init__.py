# importing the Flask class
from flask import Flask
# importing routes
from .routes import main

def create_app():
    # create the flask app
    app = Flask(__name__)

    # register blue print
    app.register_blueprint(main.bp)

    return app