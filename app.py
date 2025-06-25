# VolleyDevByMaubry [1/∞] "El corazón de la aplicación late donde el código encuentra el servidor."
from app import create_app
from datetime import datetime

app = create_app()

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

if __name__ == "__main__":
    app.run(port=3030, debug=True)
