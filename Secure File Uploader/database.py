import pymongo
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import hashlib

cluster = MongoClient("mongodb+srv://Wodiaonima38:12345@cluster0.c0zss.mongodb.net/file?retryWrites=true&w=majority")
db = cluster["file"]
collection = db["news"] 

def addUser(name, email, password):
    user = collection.find_one({"email": email})
    if user == None:
        user = {"name": name, "email": email,
                "password": hashlib.sha256(password.encode('utf-8')).hexdigest(), "photos": []}
        collection.insert_one(user)
        return {"message": "Created"}
    else:
        return {"message": "Already Exist"}



def getUser(email, password):
    user = collection.find_one(
        {"email": email, "password": hashlib.sha256(password.encode('utf-8')).hexdigest()})
    if user == None:
        return {"message": "Not Exist"}
    else:
        return user


def addphoto(email, password, photoName):
    result = collection.update_one(
        {"email": email, "password": hashlib.sha256(password.encode('utf-8')).hexdigest()}, {
            "$push": {'photos': {"filename": photoName, "date": datetime.utcnow()}}}
    ).matched_count
    if result == 1:
        return {"message": "Added"}
    else:
        return {"message": "Error"}
