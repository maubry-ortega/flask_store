# VolleyDevByMaubry [8/∞] "Rutas que guían al usuario, como senderos en un mercado digital."
import os, uuid
from bson.objectid import ObjectId
from bson.errors import InvalidId
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, current_app, render_template, redirect, url_for
from app.repositories.product_repository import ProductoRepository
from app.services.producto_service import ProductoServicio

productos_bp = Blueprint("productos", __name__)

CARGAR_CARPETA = "app/static/img"
EXTENCIONES_PERMITIDAS = {".jpg", ".jpeg", ".png", ".webp"}

def guardar_imagen(archivo): 
    if not archivo or archivo.filename == "":
        return ""
    
    extencion = os.path.splitext(archivo.filename)[1].lower()
    if extencion not in EXTENCIONES_PERMITIDAS:
        return "Extensión no permitida."
    
    nombre_archivo = secure_filename(f"{uuid.uuid4().hex}{extencion}")
    path_archivo = os.path.join(CARGAR_CARPETA, nombre_archivo)
    archivo.save(path_archivo)
    return f"/static/img/{nombre_archivo}"

def obtener_servicio():
    repositorio = ProductoRepository(current_app.db)
    return ProductoServicio(repositorio)

# --- API JSON ---
@productos_bp.route("/api", methods=["GET"])
def obtener_productos():
    servicio = obtener_servicio()
    return jsonify(servicio.listar_productos())

@productos_bp.route("/api/<producto_id>", methods=["GET"])
def obtener_producto(producto_id):
    try:
        if not ObjectId.is_valid(producto_id):
            raise InvalidId()
        servicio = obtener_servicio()
        producto = servicio.obtener_producto_por_id(producto_id)
        return jsonify(producto) if producto else ("Not Found", 404)
    except InvalidId:
        return jsonify({"error": "ID inválido"}), 400
    except Exception:
        return jsonify({"error": "Error interno"}), 500

@productos_bp.route("/api", methods=["POST"])
def crear_producto():
    servicio = obtener_servicio()
    data = request.json
    result = servicio.agregar_producto(data)
    return jsonify({"mensaje": "Producto creado", "id": str(result.inserted_id)}), 201

@productos_bp.route("/api/<producto_id>", methods=["PUT"])
def actualizar(producto_id):
    servicio = obtener_servicio()
    data = request.json
    servicio.actualizar_producto(producto_id, data)
    return "actualizado con éxito", 204

@productos_bp.route("/api/<producto_id>", methods=["DELETE"])
def eliminar(producto_id):
    servicio = obtener_servicio()
    servicio.eliminar_producto(producto_id)
    return "eliminado con éxito", 204

# --- Rutas HTML ---
@productos_bp.route("/", methods=["GET"])
def redirigir_a_pagina():
    return redirect(url_for("productos.pagina_productos"))

@productos_bp.route("/pagina", methods=["GET"])
def pagina_productos():
    servicio = obtener_servicio()
    productos = servicio.listar_productos()
    return render_template("page/lista_productos.html", productos=productos)

@productos_bp.route("/pagina/crear", methods=["GET", "POST"])
def crear_producto_formulario():
    servicio = obtener_servicio()

    if request.method == "POST":
        archivo_imagen = request.files.get("foto")
        imagen_url = guardar_imagen(archivo_imagen)

        precio = request.form.get("precio")
        if not precio or not precio.replace(".", "", 1).isdigit():
            return "Precio inválido", 400

        data = {
            "codigo": request.form.get("codigo"),
            "nombre": request.form.get("nombre"),
            "precio": float(precio),
            "foto": imagen_url,
            "categoria": request.form.get("categoria"),
        }

        servicio.agregar_producto(data)
        return redirect(url_for("productos.pagina_productos"))

    return render_template("page/formulario.html")

@productos_bp.route("/pagina/editar/<producto_id>", methods=["GET", "POST"])
def editar_producto_formulario(producto_id):
    servicio = obtener_servicio()

    if request.method == "POST":
        archivo_imagen = request.files.get("foto")
        imagen_url = guardar_imagen(archivo_imagen)

        precio = request.form.get("precio")
        if not precio or not precio.replace(".", "", 1).isdigit():
            return "Precio inválido", 400

        data = {
            "codigo": request.form.get("codigo"),
            "nombre": request.form.get("nombre"),
            "precio": float(precio),
            "categoria": request.form.get("categoria"),
        }

        if imagen_url:
            data["foto"] = imagen_url

        servicio.actualizar_producto(producto_id, data)
        return redirect(url_for("productos.pagina_productos"))

    producto = servicio.obtener_producto_por_id(producto_id)
    if not producto:
        return "Producto no encontrado", 404

    return render_template("page/formulario.html", producto=producto)

@productos_bp.route("/pagina/elimina/<producto_id>", methods=["POST"])
def eliminar_producto(producto_id):
    servicio = obtener_servicio()
    servicio.eliminar_producto(producto_id)
    return redirect(url_for("productos.pagina_productos"))
