from models.database import Database

class FeedbackModel:
    def __init__(self):
        self.db = Database()

    def get_feedbacks(self):
        self.db.cursor.execute("SELECT * FROM feedbacks")
        feedbacks = self.db.cursor.fetchall()
        self.db.close()
        return feedbacks