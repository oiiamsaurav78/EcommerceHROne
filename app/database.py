from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file from root

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["ecommerce_db"]
products_collection = db["products"]
orders_collection = db["orders"]
