# VolleyDevByMaubry [5/∞] "El repositorio es el guardián que custodia y libera los tesoros de datos."
from bson.objectid import ObjectId

class ProductoRepository:
    def __init__(self, db):
        self.collection = db.productos
        
    def get_all(self):
        return list(self.collection.find())
    
    def get_by_id(self, producto_id):
        return self.collection.find_one({"_id": ObjectId(producto_id)})
    
    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    
    def update(self, producto_id, data):
        self.collection.update_one({"_id": ObjectId(producto_id)}, {"$set": data})
        
    def delete(self, producto_id):
        self.collection.delete_one({"_id": ObjectId(producto_id)})