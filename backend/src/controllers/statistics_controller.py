from flask import jsonify
from models.feedback_model import FeedbackModel

def get_statistics():
    feedback_model = FeedbackModel()
    feedbacks = feedback_model.get_feedbacks()

    # Perform data analysis on the fetched feedbacks
    total_feedbacks = len(feedbacks)
    average_rating = sum(feedback[2] for feedback in feedbacks) / len(feedbacks) if len(feedbacks) > 0 else 1

    # Return the analysis results as JSON
    return jsonify({
        'total_feedbacks': total_feedbacks,
        'average_rating': average_rating,
        # Add more analysis results as needed
    })