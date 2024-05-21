from models.database import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def verify_user(self, user_id, role):
        self.db.cursor.execute("SELECT * FROM users WHERE id=%s AND role=%s", (user_id, role))
        user = self.db.cursor.fetchone()
        self.db.close()
        return user 
