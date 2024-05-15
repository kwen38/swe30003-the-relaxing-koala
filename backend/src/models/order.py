from flask import current_app as app
from models.user import Customer, Staff

def create_order_table():
    cursor = app.mysql.connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            items TEXT,
            total FLOAT,
            timestamp DATETIME,
            customer_name VARCHAR(255),
            customer_email VARCHAR(255),
            customer_phone VARCHAR(20),
            in_restaurant BOOLEAN DEFAULT FALSE  -- Boolean column for in-restaurant orders,
            status TEXT
        )
    """)
    app.mysql.connection.commit()
    cursor.close()

def submit_order(customer_id, order_data):
    customer = Customer.get_by_id(customer_id)
    if customer:
        items = ','.join([f"{item['name']}:{item['price']}:{item['quantity']}" for item in order_data['items']])
        total = order_data['total']
        timestamp = order_data['timestamp']
        in_restaurant = order_data.get('in_restaurant', False)
        cursor = app.mysql.connection.cursor()
        cursor.execute("INSERT INTO orders (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (items, total, timestamp, customer.name, customer.email, customer.phone, in_restaurant, 'pending'))
        app.mysql.connection.commit()
        cursor.close()
        return {'message': 'Order submitted successfully'}
    else:
        return {'error': 'Customer not found'}

def approve_order(staff_id, order_id):
    staff = Staff.get_by_id(staff_id)
    if staff:
        cursor = app.mysql.connection.cursor()
        cursor.execute("UPDATE orders SET status = 'approved' WHERE id = %s", (order_id,))
        app.mysql.connection.commit()
        cursor.close()
        return {'message': 'Order approved successfully'}
    else:
        return {'error': 'Staff member not found'}

def get_order_history():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    return orders
