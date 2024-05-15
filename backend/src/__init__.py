from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Connect to MySql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@",
    database="koala_cafe"
)

cursor = conn.cursor()

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
        in_restaurant BOOLEAN DEFAULT FALSE,  -- Boolean column for in-restaurant orders
        status VARCHAR(255)
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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        role VARCHAR(50) NOT NULL
    )
 """)

conn.commit()

# Import and register blueprints
from controllers.menu_routes import menu_blueprint
app.register_blueprint(menu_blueprint, url_prefix='/menu')

from controllers.reservation_routes import reservation_blueprint
app.register_blueprint(reservation_blueprint, url_prefix='/reservations')

from controllers.order_routes import order_blueprint
app.register_blueprint(order_blueprint, url_prefix='/orders')

from controllers.feedback_routes import feedback_blueprint
app.register_blueprint(feedback_blueprint, url_prefix='/feedbacks')

if __name__ == '__main__':
    app.run(debug=True)
