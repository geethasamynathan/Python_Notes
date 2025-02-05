from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to a database
db = client["sampledb"]

# Create or connect to a collection (table equivalent in RDBMS)
collection = db["employee"]

print("Connected to MongoDB!")

user = {"name": "John Doe", "age": 30, "city": "New York"}
insert_result = collection.insert_one(user)

print("Inserted ID:", insert_result.inserted_id)
