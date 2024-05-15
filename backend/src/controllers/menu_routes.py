from flask import Blueprint, jsonify
from models.menu import get_menu

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/', methods=['GET'])
def get_menu_items():
    items = get_menu()
    return jsonify([{'id': item[0], 'name': item[1]} for item in items])
