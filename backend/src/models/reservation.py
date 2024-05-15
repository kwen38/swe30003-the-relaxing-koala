from flask import current_app as app

def create_reservation_table():
    cursor = app.mysql.connection.cursor()
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
    app.mysql.connection.commit()
    cursor.close()

def create_reservation(data):
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']
    cursor = app.mysql.connection.cursor()
    cursor.execute("INSERT INTO reservations (name, email, phone, reservation_date, reservation_time, party_size) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, phone, reservation_date, reservation_time, party_size))
    app.mysql.connection.commit()
    cursor.close()
    return {'message': 'Reservation created successfully'}

def get_reservations():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    cursor.close()
    return reservations

def edit_reservation(reservation_id, data):
    name = data['name']
    email = data['email']
    phone = data['phone']
    reservation_date = data['reservation_date']
    reservation_time = data['reservation_time']
    party_size = data['party_size']
    cursor = app.mysql.connection.cursor()
    cursor.execute("UPDATE reservations SET name=%s, email=%s, phone=%s, reservation_date=%s, reservation_time=%s, party_size=%s WHERE id=%s", (name, email, phone, reservation_date, reservation_time, party_size, reservation_id))
    app.mysql.connection.commit()
    cursor.close()
    return {'message': 'Reservation updated successfully'}

def delete_reservation(reservation_id):
    cursor = app.mysql.connection.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=%s", (reservation_id,))
    app.mysql.connection.commit()
    cursor.close()
    return {'message': 'Reservation deleted successfully'}
