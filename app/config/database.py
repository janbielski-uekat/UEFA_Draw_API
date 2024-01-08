from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://janbielski:AhkDmkfWKhn6sa52@myfreecluster.k05ww.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.uefa_draw_db

collection_name = db["teams_collection"]