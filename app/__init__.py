# VolleyDevByMaubry [3/∞] "Desde el núcleo, se forja la estructura de un mundo digital."
from flask import Flask
from app.config import Config
from app.extensions import init_mongo
from app.routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones como la DB
    init_mongo(app)

    # Registrar Blueprints
    register_blueprints(app)

    return app