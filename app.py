# VolleyDevByMaubry [1/∞] "El corazón de la aplicación late donde el código encuentra el servidor."
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=3030, debug=True)
