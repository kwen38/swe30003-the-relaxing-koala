from flask import current_app as app

def submit_order(data):
    items = ','.join([f"{item['name']}:{item['price']}:{item['quantity']}" for item in data['items']])
    total = data['total']
    timestamp = data['timestamp']
    customer_name = data['customer_name']
    customer_email = data['customer_email']
    customer_phone = data['customer_phone']
    in_restaurant = data.get('in_restaurant', False)
    cursor = app.mysql.connection.cursor()
    cursor.execute("INSERT INTO orders (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s)", (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant))
    app.mysql.connection.commit()
    cursor.close()
    return {'message': 'Order submitted successfully'}

def get_order_history():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    return orders
