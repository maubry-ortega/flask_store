from app.cliente_mongo import db
from bson.objectid import ObjectId

productos_col = db["productos"]

def agregar_producto(data):
    return productos_col.insert_one(data)

def obtener_producto_por_codigo(codigo):
    return productos_col.find_one({"codigo": codigo})

def listar_productos():
    return list(productos_col.find())

def actualizar_producto(codigo, data):
    return productos_col.update_one({"codigo": codigo}, {"$set": data})

def eliminar_producto(codigo):
    return productos_col.delete_one({"codigo": codigo})
