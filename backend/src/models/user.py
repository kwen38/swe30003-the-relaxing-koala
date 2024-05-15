class User:
    def __init__(self, id, name, email, phone, role):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role

    @staticmethod
    def get_by_id(user_id):
        cursor = app.mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            user_id, name, email, phone, role = user_data
            if role == 'customer':
                return Customer(user_id, name, email, phone)
            elif role == 'staff':
                return Staff(user_id, name, email, phone)
        return None

class Customer(User):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone, 'customer')

    def view_menu(self):
        from models.menu import get_menu
        return get_menu()

    def submit_order(self, order_data):
        from models.order import submit_order
        return submit_order(self.id, order_data)

class Staff(User):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone, 'staff')

    def approve_order(self, order_id):
        from models.order import approve_order
        return approve_order(self.id, order_id)
