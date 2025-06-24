# VolleyDevByMaubry [15/∞] "El alma programática del sistema, donde los datos fluyen como pulsos de una API viva."

from flask import request, jsonify, current_app
from bson.objectid import ObjectId
from bson.errors import InvalidId
from app.services.producto_service import ProductoServicio
from app.repositories.product_repository import ProductoRepository

def obtener_servicio():
    return ProductoServicio(ProductoRepository(current_app.db))

def register_api_routes(bp):
    @bp.route("/api", methods=["GET"])
    def obtener_productos():
        return jsonify(obtener_servicio().listar_productos())

    @bp.route("/api/<producto_id>", methods=["GET"])
    def obtener_producto(producto_id):
        try:
            if not ObjectId.is_valid(producto_id):
                raise InvalidId()
            producto = obtener_servicio().obtener_producto_por_id(producto_id)
            return jsonify(producto) if producto else ("Not Found", 404)
        except InvalidId:
            return jsonify({"error": "ID inválido"}), 400
        except Exception:
            return jsonify({"error": "Error interno"}), 500

    @bp.route("/api", methods=["POST"])
    def crear_producto():
        data = request.json
        result = obtener_servicio().agregar_producto(data)
        return jsonify({"mensaje": "Producto creado", "id": str(result.inserted_id)}), 201

    @bp.route("/api/<producto_id>", methods=["PUT"])
    def actualizar(producto_id):
        obtener_servicio().actualizar_producto(producto_id, request.json)
        return "", 204

    @bp.route("/api/<producto_id>", methods=["DELETE"])
    def eliminar(producto_id):
        obtener_servicio().eliminar_producto(producto_id)
        return "", 204
