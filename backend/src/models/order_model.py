from models.database import Database

class OrderModel:
    def __init__(self):
        self.db = Database()

    def submit_order(self, items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant):
        items_str = ','.join([f"{item['name']}:{item['price']}:{item['quantity']}" for item in items])
        self.db.cursor.execute("INSERT INTO orders (items, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                (items_str, total, timestamp, customer_name, customer_email, customer_phone, in_restaurant))
        self.db.commit()
        self.db.close()

    def get_order_history(self):
        self.db.cursor.execute("SELECT * FROM orders")
        orders = self.db.cursor.fetchall()
        self.db.close()
        return orders