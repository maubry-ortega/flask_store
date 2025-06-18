from flask import Flask, render_template
from .routes.productos import productos_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(productos_bp, url_prefix="/productos")
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    return app 
