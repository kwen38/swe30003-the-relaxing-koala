from flask import jsonify
from models.menu_model import MenuModel

def get_menu():
    menu_model = MenuModel()
    items = menu_model.get_menu()
    return jsonify([{'id': item[0], 'name': item[1]} for item in items])