# VolleyDevByMaubry [6/∞] "El servicio teje la lógica que da vida a la experiencia del usuario."
class ProductoServicio:
    def __init__(self, repository):
        self.repository = repository

    def agregar_producto(self, data):
        return self.repository.create(data)

    def obtener_producto_por_id(self, producto_id):
        return self.repository.get_by_id(producto_id)

    def listar_productos(self):
        return self.repository.get_all()

    def actualizar_producto(self, producto_id, data):
        self.repository.update(producto_id, data)

    def eliminar_producto(self, producto_id):
        self.repository.delete(producto_id)
