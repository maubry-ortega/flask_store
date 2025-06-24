# VolleyDevByMaubry [12/∞] "Extensiones que conectan las venas del sistema con su esencia técnica."

from pymongo import MongoClient

def init_mongo(app):
    mongo_client = MongoClient(app.config["MONGO_URI"])
    app.db = mongo_client[app.config["MONGO_DB_NAME"]]
