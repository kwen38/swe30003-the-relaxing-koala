import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="[insert_pw]",
            database="koala_cafe"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                id INT AUTO_INCREMENT PRIMARY KEY,
                items TEXT
            )
        """)

        self.cursor.execute("""
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

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                items TEXT,
                total FLOAT,
                timestamp DATETIME,
                customer_name VARCHAR(255),
                customer_email VARCHAR(255),
                customer_phone VARCHAR(20),
                in_restaurant BOOLEAN DEFAULT FALSE,
                status VARCHAR(255)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedbacks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT,
            rating INT,
            comment TEXT,
            timestamp DATETIME,
            FOREIGN KEY (order_id) REFERENCES orders(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                role VARCHAR(50) NOT NULL
            )
        """)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
