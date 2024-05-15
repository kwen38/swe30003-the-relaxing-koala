from flask import current_app as app

def create_feedback_table():
    cursor = app.mysql.connection.cursor()
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
    app.mysql.connection.commit()
    cursor.close()

def get_statistics():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM feedbacks")
    feedbacks = cursor.fetchall()
    cursor.close()

    total_feedbacks = len(feedbacks)
    average_rating = sum(feedback[2] for feedback in feedbacks) / len(feedbacks) if len(feedbacks) > 0 else 1

    return {
        'total_feedbacks': total_feedbacks,
        'average_rating': average_rating,
        # Add more analysis results as needed
    }
