from app.models.producto import collection_producto

class ProductoServicio:
    def __init__(self, repository):
        self.repository = repository
        
    def agregar_producto(self, data):
        return self.repository.create(data)

    def obtener_producto_por_id(self, producto_id):
        producto = self.repository.get_by_id(producto_id)
        return collection_producto(producto) if producto else None

    def listar_productos(self):
        return [collection_producto(p) for p in self.resitory.get_all()]
    
    def actualizar_producto(self, producto_id, data):
        self.repository.update(producto_id, data)

    def eliminar_producto(self, producto_id):
        return self.repository.delete(producto_id)
