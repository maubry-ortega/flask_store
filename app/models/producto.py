# VolleyDevByMaubry [4/∞] "Cada producto es un relato, modelado en código para brillar."

def modelo_producto(producto):
    if not producto:
        return None

    return {
        "id": str(producto.get("_id")),
        "codigo": producto.get("codigo"),
        "nombre": producto.get("nombre"),
        "precio": producto.get("precio"),
        "foto": producto.get("foto"),
        "categoria": producto.get("categoria"),
    }

def modelo_lista_productos(productos):
    return [modelo_producto(p) for p in productos]
