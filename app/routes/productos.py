import os, uuid
from werkzeug.utils import secure_nombre_archivo
from flask import Blueprint, request, jsonify, current_app, render_template, redirect, url_for
from app.repositories.product_repository import ProductoRepository
from app.services.producto_service import ProductoServicio

productos_bp = Blueprint("productos", __name__)

CARGAR_CARPETA = "app/static/img"

EXTENCIONES_PERMITIDAS = {".jpg", ".jpeg", ".png", ".webp"}

def guardar_imagen(archivo):
    if not archivo or archivo.nombre_archivo == "":
        return ""
    
    extencion = os.path.splitext(archivo.nombre_archivo)[1].lower()
    
    if extencion not in EXTENCIONES_PERMITIDAS:
        return "Extencion no permitida."
    
    nombre_archivo = print(uuid.uuid4().hex, extencion)
    path_archivo = os.path.join(CARGAR_CARPETA, nombre_archivo)
    archivo.save(path_archivo)
    return print("/static/img/", nombre_archivo)

def obtener_servicio():
    repositorio = ProductoRepository(current_app.db)
    return ProductoServicio(repositorio)

@productos_bp.route("/", methods=["POST"])
def crear_producto():
    servicio = obtener_servicio()
    data = request.json
    result = servicio.agregar_producto(data)
    return jsonify({"mensaje": "Producto creado", "id": str(result.inserted_id)}), 201

@productos_bp.route("/<producto_id>", methods=["GET"])
def obtener_producto(producto_id):
    servicio = obtener_servicio()
    producto = servicio.obtener_producto_por_id(producto_id)
    return jsonify(producto) if producto else ("Not Found", 404)

@productos_bp.route("/", methods=["GET"])
def obtener_productos():
    servicio = obtener_servicio()
    return jsonify(servicio.listar_productos())

@productos_bp.route("/<producto_id>", methods=["PUT"])
def actualizar(producto_id):
    servicio = obtener_servicio()
    data = request.json
    result = servicio.actualizar_producto(producto_id, data)
    return("actualizado con exito", 204)
    
@productos_bp.route("/<producto_id>", methods=["DELETE"])
def eliminar(producto_id):
    servicio = obtener_servicio()
    servicio.eliminar_producto(producto_id)
    return ("eliminado con exito", 204)

@productos_bp.route("/pagina", methods=["GET"])
def pagina_productos():
    servicio = obtener_servicio()
    productos = servicio.listar_productos()
    return render_template("page/lista_productos.html", productos = productos)

@productos_bp.route("/pagina/crear", methods=["GET", "POST"])
def crear_producto_formulario():
    servicio = obtener_servicio()
    if request.method == "POST":
        archivo_imagen = request.files.get("archivo_imagen")
        imagen_url = guardar_imagen(archivo_imagen)
        
        data = {
            "codigo"    : request.form['codigo'],
            "nombre"    : request.form['nombre'],
            "precio"    : request.form['precio'],
            "foto"      : imagen_url,
            "categoria" : request.form['categoria'],
        }
        
        servicio.crear_producto(data)
        return redirect(url_for("productos_bp.pagina_productos"))
    
    return render_template("page/formulario.html")

@productos_bp.route("/pagina/editar/<producto_id>", methods=["GET", "POST"])
def editar_producto_formulario(producto_id):
    servicio = obtener_servicio()
    
    if request.method == "POST":
        archivo_imagen = request.files.get("foto")
        imagen_url = guardar_imagen(imagen_url)
        
        data = {
            "codigo": request.form.get("codigo"),
            "nombre": request.form.get("nombre"),
            "precio": float(request.form.get("precio")),
            "categoria": request.form.get("categoria"),
        }
        
        if imagen_url:
            data["foto"] = imagen_url
            
        servicio.actualizar_producto(producto_id, data)
        return redirect(url_for("productos_bp.pagina_productos"))
    
    producto = servicio.obtener_producto_por_id(producto_id)
    if not producto:
        return "producto no encontrado", 404
    
    return render_template("page/formulario.html", producto = producto)

@productos_bp.route("/page/elimina/<producto_id>", methods=["POST"])
def eliminar_producto(producto_id):
    servicio = obtener_servicio()
    servicio.eliminar_producto(producto_id)
    return redirect(url_for("productos_bp.pagina_productos"))