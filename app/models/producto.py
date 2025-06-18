def collection_producto(doc):
    return {
        "id": str(doc["_id"]),
        "codigo": doc["codigo"],
        "nombre": doc["nombre"],
        "precio": doc["precio"],
        "foto": doc["foto"],
        "categoria": doc["categoria"]
    }
