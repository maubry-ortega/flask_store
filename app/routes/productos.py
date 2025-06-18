from flask import Blueprint, request, jsonify
from app.services import producto_service
from app.models.producto import collection_producto

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/", methods=["POST"])
def crear_producto():
    data = request.json
    result = producto_service.agregar_producto(data)
    return jsonify({"mensaje": "Producto creado", "id": str(result.inserted_id)}), 201

@productos_bp.route("/<codigo>", methods=["GET"])
def obtener_producto(codigo):
    producto = producto_service.obtener_producto_por_codigo(codigo)
    if producto:
        return jsonify(collection_producto(producto))
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@productos_bp.route("/", methods=["GET"])
def obtener_productos():
    productos = producto_service.listar_productos()
    return jsonify([collection_producto(p) for p in productos])

@productos_bp.route("/<codigo>", methods=["PUT"])
def actualizar(codigo):
    data = request.json
    result = producto_service.actualizar_producto(codigo, data)
    if result.matched_count:
        return jsonify({"mensaje": "Producto actualizado"})
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@productos_bp.route("/<codigo>", methods=["DELETE"])
def eliminar(codigo):
    result = producto_service.eliminar_producto(codigo)
    if result.deleted_count:
        return jsonify({"mensaje": "Producto eliminado"})
    return jsonify({"mensaje": "Producto no encontrado"}), 404
