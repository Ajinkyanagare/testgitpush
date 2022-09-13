import pymongo
client = pymongo.MongoClient("mongodb+srv://Ajinkya:7028435990@cluster0.fxza7.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"Ajinkya",
    "email_id" : "ajinkya@gmail.com",
"surname": "nagare"}

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)

