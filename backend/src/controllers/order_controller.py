from flask import jsonify, request
from models.order_model import OrderModel

def submit_order():
    data = request.get_json()
    items = data['items']
    total = data['total']
    timestamp = data['timestamp']
    customer_name = data['customer_name']
    customer_email = data['customer_email']
    customer_phone = data['customer_phone']
    in_restaurant = data.get('in_restaurant', False)

    order_model = OrderModel()
    order_model.submit_order(items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant)
    return jsonify({'message': 'Order submitted successfully'}), 201

def get_order_history():
    order_model = OrderModel()
    orders = order_model.get_order_history()
    return jsonify([{'id': order[0], 'items': [{'name': item.split(':')[0], 'price': float(item.split(':')[1]), 'quantity': int(item.split(':')[2])} for item in order[1].split(',')], 'total': order[2], 'timestamp': str(order[3]), 'customer_name': order[4], 'customer_email': order[5], 'customer_phone': order[6]} for order in orders])