from flask import Blueprint, request, jsonify
from models.order import submit_order, get_order_history

order_blueprint = Blueprint('orders', __name__)

@order_blueprint.route('/', methods=['POST'])
def submit_new_order():
    data = request.get_json()
    result = submit_order(data)
    return jsonify(result), 201

@order_blueprint.route('/history', methods=['GET'])
def get_order_history_data():
    orders = get_order_history()
    return jsonify([{'id': order[0], 'items': [{'name': item.split(':')[0], 'price': float(item.split(':')[1]), 'quantity': int(item.split(':')[2])} for item in order[1].split(',')], 'total': order[2], 'timestamp': str(order[3]), 'customer_name': order[4], 'customer_email': order[5], 'customer_phone': order[6]} for order in orders])
