# VolleyDevByMaubry [13/∞] "Las rutas se entrelazan aquí, como hilos que trazan el mapa del sistema."

from app.routes.productos import productos_bp

def register_blueprints(app):
    app.register_blueprint(productos_bp, url_prefix="/")
