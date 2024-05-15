from flask import Blueprint, jsonify
from models.feedback import get_statistics

feedback_blueprint = Blueprint('feedback', __name__)

@feedback_blueprint.route('/statistics', methods=['GET'])
def get_statistics_data():
    statistics = get_statistics()
    return jsonify(statistics)
