from models.database import Database

class ReservationModel:
    def __init__(self):
        self.db = Database()

    def create_reservation(self, name, email, phone, reservation_date, reservation_time, party_size):
        self.db.cursor.execute("INSERT INTO reservations (name, email, phone, reservation_date, reservation_time, party_size) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, phone, reservation_date, reservation_time, party_size))
        self.db.commit()
        self.db.close()

    def get_reservations(self):
        self.db.cursor.execute("SELECT * FROM reservations")
        reservations = self.db.cursor.fetchall()
        self.db.close()
        return reservations

    def edit_reservation(self, reservation_id, name, email, phone, reservation_date, reservation_time, party_size):
        self.db.cursor.execute("UPDATE reservations SET name=%s, email=%s, phone=%s, reservation_date=%s, reservation_time=%s, party_size=%s WHERE id=%s", (name, email, phone, reservation_date, reservation_time, party_size, reservation_id))
        self.db.commit()
        self.db.close()

    def delete_reservation(self, reservation_id):
        self.db.cursor.execute("DELETE FROM reservations WHERE id=%s", (reservation_id,))
        self.db.commit()
        self.db.close()