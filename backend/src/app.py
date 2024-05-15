from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@",
    database="koala_cafe"
)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        id INT AUTO_INCREMENT PRIMARY KEY,
        items TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(20),
        reservation_date DATE,
        reservation_time TIME,
        party_size INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        items TEXT,
        total FLOAT,
        timestamp DATETIME,
        customer_name VARCHAR(255),
        customer_email VARCHAR(255),
        customer_phone VARCHAR(20),
        in_restaurant BOOLEAN DEFAULT FALSE  -- Boolean column for in-restaurant orders
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedbacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    rating INT,
    comment TEXT,
    timestamp DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(id)
    )
""")

conn.commit()

@app.route('/menu', methods=['GET'])
def get_menu():
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    return jsonify([{'id': item[0], 'name': item[1]} for item in items])

@app.route('/submit-order', methods=['POST'])
def submit_order():
    data = request.get_json()
    items = ','.join([f"{item['name']}:{item['price']}:{item['quantity']}" for item in data['items']])
    total = data['total']
    timestamp = data['timestamp']
    customer_name = data['customer_name']
    customer_email = data['customer_email']
    customer_phone = data['customer_phone']
    in_restaurant = data.get('in_restaurant', False)
    cursor.execute("INSERT INTO orders (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant))
    conn.commit()
    return jsonify({'message': 'Order submitted successfully'}), 201

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']
    cursor.execute("INSERT INTO reservations (name, email, phone, reservation_date, reservation_time, party_size) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, phone, reservation_date, reservation_time, party_size))
    conn.commit()
    return jsonify({'message': 'Reservation created successfully'}), 201

@app.route('/manage-reservations', methods=['GET'])
def get_reservations():
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    return jsonify([{'id': reservation[0], 'name': reservation[1], 'email': reservation[2], 'phone': reservation[3], 'reservation_date': str(reservation[4]), 'reservation_time': str(reservation[5]), 'party_size': reservation[6]} for reservation in reservations])

@app.route('/edit-reservation/<int:reservation_id>', methods=['PUT'])
def edit_reservation(reservation_id):
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']
    cursor.execute("UPDATE reservations SET name=%s, email=%s, phone=%s, reservation_date=%s, reservation_time=%s, party_size=%s WHERE id=%s", (name, email, phone, reservation_date, reservation_time, party_size, reservation_id))
    conn.commit()
    return jsonify({'message': 'Reservation updated successfully'}), 200

@app.route('/delete-reservation/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    cursor.execute("DELETE FROM reservations WHERE id=%s", (reservation_id,))
    conn.commit()
    return jsonify({'message': 'Reservation deleted successfully'}), 200

@app.route('/history', methods=['GET'])
def get_order_history():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    return jsonify([{'id': order[0], 'items': [{'name': item.split(':')[0], 'price': float(item.split(':')[1]), 'quantity': int(item.split(':')[2])} for item in order[1].split(',')], 'total': order[2], 'timestamp': str(order[3]), 'customer_name': order[4], 'customer_email': order[5], 'customer_phone': order[6]} for order in orders])

@app.route('/statistics', methods=['GET'])
def get_statistics():
    # Fetch data from the feedback table for analysis
    cursor.execute("SELECT * FROM feedbacks")
    feedbacks = cursor.fetchall()

    # Perform data analysis on the fetched feedbacks
    # (Add your analysis logic here)
    total_feedbacks = len(feedbacks)
    average_rating = sum(feedback[2] for feedback in feedbacks) / len(feedbacks) if len(feedbacks) > 0 else 1

    # Return the analysis results as JSON
    return jsonify({
        'total_feedbacks': total_feedbacks,
        'average_rating': average_rating,
        # Add more analysis results as needed
    })

if __name__ == '__main__':
    app.run(debug=True)
