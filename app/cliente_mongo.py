from pymongo import MongoClient
from config import Config

mongo_client = MongoClient(Config.MONGO_URI)
db = mongo_client["tiendaorm"]