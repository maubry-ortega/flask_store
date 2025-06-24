# VolleyDevByMaubry [17/∞] "Pequeñas funciones, grandes aliados silenciosos del sistema."

import os, uuid
from werkzeug.utils import secure_filename

CARGAR_CARPETA = "app/static/img"
EXTENCIONES_PERMITIDAS = {".jpg", ".jpeg", ".png", ".webp"}

def guardar_imagen(archivo):
    if not archivo or archivo.filename == "":
        return ""

    extencion = os.path.splitext(archivo.filename)[1].lower()
    if extencion not in EXTENCIONES_PERMITIDAS:
        return ""

    nombre_archivo = secure_filename(f"{uuid.uuid4().hex}{extencion}")
    path_archivo = os.path.join(CARGAR_CARPETA, nombre_archivo)
    archivo.save(path_archivo)
    return f"/static/img/{nombre_archivo}"

def validar_precio(valor):
    try:
        return float(valor)
    except (TypeError, ValueError):
        return None
