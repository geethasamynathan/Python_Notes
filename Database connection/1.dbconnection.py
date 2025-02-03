import mysql.connector
from mysql.connector import Error

# Database Connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change as per your MySQL username
            password='root@123',  # Change as per your MySQL password
            database='testdb'
        )
        if connection.is_connected():
            print("Connected to MySQL")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
def create_user(name, email):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))
            connection.commit()
            print("User added successfully")
    except Error as e:
        print(f"Failed to insert record: {e}")
    finally:
        if connection:
            connection.close()

name=input('Enter the username');
email=input('Enter the email')
create_user(name,email)

def get_users():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()
            for row in records:
                print(row)
    except Error as e:
        print(f"Failed to retrieve records: {e}")
    finally:
        if connection:
            connection.close()
            
get_users()