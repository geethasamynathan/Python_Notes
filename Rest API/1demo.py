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