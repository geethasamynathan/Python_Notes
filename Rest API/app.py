from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL Configuration
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='api_db'
)
cursor = conn.cursor()

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    age = data['age']
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    conn.commit()
    return jsonify({"message": "User added successfully"}), 201

# 2. Get All Users (GET)

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

# 3. Get User by ID (GET)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

#4. Update User (PUT)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    name = data['name']
    email = data['email']
    age = data['age']
    cursor.execute("UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, age, id))
    conn.commit()
    return jsonify({"message": "User updated successfully"})

#5. Delete User (DELETE)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)