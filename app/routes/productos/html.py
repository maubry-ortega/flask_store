# VolleyDevByMaubry [16/∞] "La capa visible del sistema, donde el código se transforma en experiencia."

from flask import render_template, request, redirect, url_for, current_app
from app.services.producto_service import ProductoServicio
from app.repositories.product_repository import ProductoRepository
from .utils import guardar_imagen, validar_precio
from app.models.producto import modelo_lista_productos

def obtener_servicio():
    return ProductoServicio(ProductoRepository(current_app.db))

def register_html_routes(bp):
    @bp.route("/", methods=["GET"])
    def home():
        return redirect(url_for("productos.pagina_productos"))

    @bp.route("/pagina", methods=["GET"])
    def pagina_productos():
        productos_raw = obtener_servicio().listar_productos()
        productos = modelo_lista_productos(productos_raw)
        return render_template("page/lista_productos.html", productos=productos)
    
    @bp.route("/pagina/crear", methods=["GET", "POST"])
    def crear_producto_formulario():
        if request.method == "POST":
            imagen_url = guardar_imagen(request.files.get("foto"))
            precio = validar_precio(request.form.get("precio"))
            if precio is None:
                return "Precio inválido", 400

            data = {
                "codigo": request.form.get("codigo"),
                "nombre": request.form.get("nombre"),
                "precio": precio,
                "foto": imagen_url,
                "categoria": request.form.get("categoria"),
            }

            obtener_servicio().agregar_producto(data)
            return redirect(url_for("productos.pagina_productos"))

        return render_template("page/formulario.html")

    @bp.route("/pagina/editar/<producto_id>", methods=["GET", "POST"])
    def editar_producto_formulario(producto_id):
        servicio = obtener_servicio()
        if request.method == "POST":
            imagen_url = guardar_imagen(request.files.get("foto"))
            precio = validar_precio(request.form.get("precio"))
            if precio is None:
                return "Precio inválido", 400

            data = {
                "codigo": request.form.get("codigo"),
                "nombre": request.form.get("nombre"),
                "precio": precio,
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

    @bp.route("/pagina/elimina/<producto_id>", methods=["POST"])
    def eliminar_producto(producto_id):
        obtener_servicio().eliminar_producto(producto_id)
        return redirect(url_for("productos.pagina_productos"))
