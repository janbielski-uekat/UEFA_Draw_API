from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

uri = os.getenv('DB_CONNECTION_STRING')

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.uefa_draw_db

collection_name = db["teams_collection"]