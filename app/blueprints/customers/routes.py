from flask import Blueprint, request, jsonify

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    # Logic to retrieve customers
    return jsonify({"message": "List of customers"})

@customers_bp.route('/customers', methods=['POST'])
def add_customer():
    # Logic to add a new customer
    data = request.get_json()
    return jsonify({"message": "Customer added", "data": data}), 201

@customers_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    # Logic to retrieve a specific customer by ID
    return jsonify({"message": f"Customer {customer_id}"})

@customers_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    # Logic to update a specific customer by ID
    data = request.get_json()
    return jsonify({"message": f"Customer {customer_id} updated", "data": data})

@customers_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    # Logic to delete a specific customer by ID
    return jsonify({"message": f"Customer {customer_id} deleted"})