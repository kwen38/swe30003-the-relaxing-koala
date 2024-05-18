from models.database import Database

class MenuModel:
    def __init__(self):
        self.db = Database()

    def get_menu(self):
        self.db.cursor.execute("SELECT * FROM menu")
        items = self.db.cursor.fetchall()
        self.db.close()
        return items