from flask import Blueprint, request, jsonify

mechanics_bp = Blueprint('mechanics', __name__)

@mechanics_bp.route('/mechanics', methods=['GET'])
def get_mechanics():
    # Logic to get mechanics
    return jsonify({"message": "List of mechanics"})

@mechanics_bp.route('/mechanics', methods=['POST'])
def add_mechanic():
    # Logic to add a new mechanic
    data = request.get_json()
    return jsonify({"message": "Mechanic added", "data": data}), 201