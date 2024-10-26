from flask import Blueprint, request, jsonify

service_tickets_bp = Blueprint('service_tickets', __name__)

@service_tickets_bp.route('/service_tickets', methods=['GET'])
def get_service_tickets():
    # Logic to get service tickets
    return jsonify({"message": "List of service tickets"})

@service_tickets_bp.route('/service_tickets', methods=['POST'])
def create_service_ticket():
    # Logic to create a new service ticket
    data = request.get_json()
    return jsonify({"message": "Service ticket created", "data": data}), 201

@service_tickets_bp.route('/service_tickets/<int:ticket_id>', methods=['PUT'])
def update_service_ticket(ticket_id):
    # Logic to update a service ticket
    data = request.get_json()
    return jsonify({"message": f"Service ticket {ticket_id} updated", "data": data})

@service_tickets_bp.route('/service_tickets/<int:ticket_id>', methods=['DELETE'])
def delete_service_ticket(ticket_id):
    # Logic to delete a service ticket
    return jsonify({"message": f"Service ticket {ticket_id} deleted"})