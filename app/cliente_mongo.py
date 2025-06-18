from pymongo import MongoClient
from app.config import Config

mongo_client = MongoClient(Config.MONGO_URI)
db = mongo_client["tiendaorm"]