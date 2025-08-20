from flask import Flask
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi, os

app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
uri = "mongodb+srv://crisesv4:Tanke1804.@cluster0.ejxv3jy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client["BlueSwitchData"]

# Colecciones (para que todos los endpoints puedan usarlas)
userscollection = db["Users"]
devicescollection = db["Devices"]
discardDevicesCollection = db["discardDevices"]
teamscollection = db["Teams"]

@app.route("/", methods=["GET"])
def hello():
    return {"mensaje": "Hello, World!"}