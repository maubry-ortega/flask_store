# VolleyDevByMaubry [14/∞] "Aquí convergen las dos caras del sistema: la lógica API y la experiencia visual."

from flask import Blueprint
from .api import register_api_routes
from .html import register_html_routes

productos_bp = Blueprint("productos", __name__)

register_api_routes(productos_bp)
register_html_routes(productos_bp)
