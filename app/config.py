# VolleyDevByMaubry [2/∞] "Las claves del universo se guardan en variables silenciosas."
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")