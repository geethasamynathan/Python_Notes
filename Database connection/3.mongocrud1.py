from pymongo import MongoClient

def connect_db():
    try:
        client=MongoClient("mongodb://localhost:27017/")
        db=client["CMR_DB"]
        print("Mongodb Connected Successfully")
        return db
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def create_Collection(db):
    try:
        db.create_collection("employee")
        print("Table Created Successfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        
def insert_data(db):
    try:
        collection=db["employee"]
        n=int(input("Enter the no of records to be inserted:"))
        data=[]
        for i in range(n):
            name=input("Enter the name of employee:")
            age=int(input("Enter the age of the employee:"))
            email=input("Enter the email:")
            city=input("Enter the city:")
            skills=[]
            n1=int(input("Enter the no of skills you have:"))
            for j in range(n1):
                skill=input("Enter the skill:")
                skills.append(skill)
            skill_str=', '.join(skills)
            data.append({"name":name,"age":age,"email":email,"city":city,"skills":skill_str})
        collection.insert_many(data)
        print("Data Inserted Succesfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def select_all(db):
    try:
        collection=db["employee"]
        data=collection.find()
        for res in data:
            print(res)
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def update_data(db):
    try:
        collection=db["employee"]
        name=input("Enter the name of the employee you want to update:")
        query={"name":name}
        new_values={"$set":{"email":"redyshanmuka67@gmail.com"}}
        collection.update_one(query,new_values)
        print("Updated the new data succesfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def delete_data(db):
    try:
        collection=db["employee"]
        name=input("Enter the name of the employee you want to delete:")
        query={"name":name}
        collection.delete_one(query)
        print("Record deleted succesfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None

def delete_collection(db):
    try:
        collection=db["employee"]
        collection.drop()
        print("Collection deleted succesfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def filtering_data(db):
    try:
        collection=db["employee"]
        query={"age":{"$gte":20}}
        data=collection.find(query)
        for res in data:
            print(res)
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def sort_data(db):
    try:
        collection=db["employee"]
        query={"age":{"$gt":20}}
        data=collection.find(query).sort("age")
        for res in data:
            print(res)
    except Exception as err:
        print(f"Something went wrong:{err}")
        return None
    
def drop_database():
    try:
        client=MongoClient("mongodb://localhost:27017/")
        client.drop_database("CMR_DB")
        print("Database deleted succesfully")
    except Exception as err:
        print(f"Something went wrong:{err}")
        
def main():
    db=connect_db()
    if db is None:
        print("Database not connected")
    # create_Collection(db)
    # insert_data(db)
    # update_data(db)
    # delete_data(db)
    # filtering_data(db)
    # sort_data(db)
    # delete_collection(db)
    drop_database()

main()