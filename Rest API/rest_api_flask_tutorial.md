# REST API with Flask

## What is a REST API?
A **REST API** (Representational State Transfer API) is a set of rules that allows communication between different systems over the web using HTTP methods like **GET, POST, PUT, DELETE**. It follows a client-server architecture and uses stateless communication.

## Why REST API?
Imagine you have a **mobile app and a web application** that need to access the same backend data (like user details or orders). Instead of writing separate backend logic for each, you can create a **REST API** that acts as a bridge between the frontend and backend. 

REST APIs are widely used because they are:
- **Lightweight**: Uses simple HTTP methods.
- **Scalable**: Can handle multiple clients like mobile apps, web apps, and IoT devices.
- **Stateless**: Each request is independent, making it efficient.

## A Story for Why Web API?
### The Pizza Shop Problem
Imagine **John** owns a pizza shop. He starts by taking orders over the phone and noting them on paper. As his business grows:
1. He builds a **website** where customers can place orders.
2. He creates a **mobile app** so customers can order on the go.
3. He partners with **delivery services** that need real-time order data.

Instead of managing **separate backends** for the website, mobile app, and delivery partners, he **creates a REST API**:
- **Website** calls `GET /menu` to show pizzas.
- **Mobile app** calls `POST /order` to place an order.
- **Delivery service** calls `GET /orders` to fetch new orders.

Now, **one backend** (REST API) serves all **three** clients efficiently.

---

## Simple REST API Example Using Flask (Step-by-Step)
Flask is a lightweight Python framework to create web APIs quickly.

### Step 1: Install Flask
First, install Flask if you haven't:
```bash
pip install flask
```

### Step 2: Create a Simple REST API
Create a new Python file, e.g., `app.py`, and write the following code:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (simulating a database)
pizzas = [
    {"id": 1, "name": "Margherita", "price": 8.99},
    {"id": 2, "name": "Pepperoni", "price": 10.99}
]

# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    return jsonify(pizzas)  # Convert Python list to JSON

# Route to get a single pizza by ID
@app.route('/pizzas/<int:pizza_id>', methods=['GET'])
def get_pizza(pizza_id):
    pizza = next((p for p in pizzas if p["id"] == pizza_id), None)
    if pizza:
        return jsonify(pizza)
    return jsonify({"error": "Pizza not found"}), 404

# Route to add a new pizza
@app.route('/pizzas', methods=['POST'])
def add_pizza():
    new_pizza = request.get_json()
    new_pizza["id"] = len(pizzas) + 1  # Assign an ID
    pizzas.append(new_pizza)
    return jsonify(new_pizza), 201

# Route to delete a pizza by ID
@app.route('/pizzas/<int:pizza_id>', methods=['DELETE'])
def delete_pizza(pizza_id):
    global pizzas
    pizzas = [p for p in pizzas if p["id"] != pizza_id]
    return jsonify({"message": "Pizza deleted"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3: Run the API
Run the script:
```bash
python app.py
```
You'll see an output like:
```
 * Running on http://127.0.0.1:5000/
```
Now, you can test your API.

---

### Step 4: Test the API
You can test it using **Postman** or **curl**.

#### 1. Get all pizzas:
```bash
curl http://127.0.0.1:5000/pizzas
```
**Response:**
```json
[
    {"id": 1, "name": "Margherita", "price": 8.99},
    {"id": 2, "name": "Pepperoni", "price": 10.99}
]
```

#### 2. Get a single pizza by ID:
```bash
curl http://127.0.0.1:5000/pizzas/1
```
**Response:**
```json
{"id": 1, "name": "Margherita", "price": 8.99}
```

#### 3. Add a new pizza:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Veggie", "price": 9.99}' http://127.0.0.1:5000/pizzas
```
**Response:**
```json
{"id": 3, "name": "Veggie", "price": 9.99}
```

#### 4. Delete a pizza by ID:
```bash
curl -X DELETE http://127.0.0.1:5000/pizzas/2
```
**Response:**
```json
{"message": "Pizza deleted"}
```

---

## Explanation of Code
- **`Flask(__name__)`**: Creates a Flask web server.
- **`@app.route('/pizzas', methods=['GET'])`**: Defines a GET endpoint to fetch pizzas.
- **`jsonify()`**: Converts Python objects to JSON format.
- **`request.get_json()`**: Extracts JSON data from incoming POST requests.
- **`app.run(debug=True)`**: Starts the Flask server in debug mode.

---

## Conclusion
With this simple **Flask REST API**, you now have a working backend for a pizza shop where:
- Customers can **view available pizzas** (`GET /pizzas`).
- Admins can **add new pizzas** (`POST /pizzas`).
- Users can **fetch a specific pizza** (`GET /pizzas/{id}`).
- Admins can **delete a pizza** (`DELETE /pizzas/{id}`).

This is a basic **REST API** in Flask, and it can be extended to include authentication, databases, and more.
