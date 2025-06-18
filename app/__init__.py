from flask import Flask
from app.routes.productos import productos_bp
from app.config import Config
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Mongo
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client[app.config["MONGO_DB_NAME"]]

    # Register Blueprints
    app.register_blueprint(productos_bp, url_prefix="/")

    return app