from flask import jsonify, request
from models.reservation_model import ReservationModel

def create_reservation():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']

    reservation_model = ReservationModel()
    reservation_model.create_reservation(name, email, phone, reservation_date, reservation_time, party_size)
    return jsonify({'message': 'Reservation created successfully'}), 201

def get_reservations():
    reservation_model = ReservationModel()
    reservations = reservation_model.get_reservations()
    return jsonify([{'id': reservation[0], 'name': reservation[1], 'email': reservation[2], 'phone': reservation[3], 'reservation_date': str(reservation[4]), 'reservation_time': str(reservation[5]), 'party_size': reservation[6]} for reservation in reservations])

def edit_reservation(reservation_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']

    reservation_model = ReservationModel()
    reservation_model.edit_reservation(reservation_id, name, email, phone, reservation_date, reservation_time, party_size)
    return jsonify({'message': 'Reservation updated successfully'}), 200

def delete_reservation(reservation_id):
    reservation_model = ReservationModel()
    reservation_model.delete_reservation(reservation_id)
    return jsonify({'message': 'Reservation deleted successfully'}), 200