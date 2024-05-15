from flask import Blueprint, request, jsonify
from models.reservation import create_reservation, get_reservations, edit_reservation, delete_reservation

reservation_blueprint = Blueprint('reservations', __name__)

@reservation_blueprint.route('/', methods=['POST'])
def create_new_reservation():
    data = request.get_json()
    result = create_reservation(data)
    return jsonify(result), 201

@reservation_blueprint.route('/', methods=['GET'])
def get_all_reservations():
    reservations = get_reservations()
    return jsonify([{'id': reservation[0], 'name': reservation[1], 'email': reservation[2], 'phone': reservation[3], 'reservation_date': str(reservation[4]), 'reservation_time': str(reservation[5]), 'party_size': reservation[6]} for reservation in reservations])

@reservation_blueprint.route('/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.get_json()
    result = edit_reservation(reservation_id, data)
    return jsonify(result), 200

@reservation_blueprint.route('/<int:reservation_id>', methods=['DELETE'])
def remove_reservation(reservation_id):
    result = delete_reservation(reservation_id)
    return jsonify(result), 200
