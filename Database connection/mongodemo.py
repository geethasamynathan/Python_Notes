from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

db=client['demo_cmr_db']

collection=db['employee']

print('Connnected to Mongodb')

user = {"name": "John Doe", "age": 30, "city": "New York"}
insert_result = collection.insert_one(user)

print("Inserted ID:", insert_result.inserted_id)

for user in collection.find():
    print(user)