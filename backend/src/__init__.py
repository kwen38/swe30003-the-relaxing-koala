from flask import Flask
from controllers import (
    menu_controller,
    order_controller,
    reservation_controller,
    statistics_controller,
)

app = Flask(__name__)

# Register routes
app.route('/menu', methods=['GET'])(menu_controller.get_menu)
app.route('/submit-order', methods=['POST'])(order_controller.submit_order)
app.route('/reservations', methods=['POST'])(reservation_controller.create_reservation)
app.route('/manage-reservations', methods=['GET'])(reservation_controller.get_reservations)
app.route('/edit-reservation/<int:reservation_id>', methods=['PUT'])(reservation_controller.edit_reservation)
app.route('/delete-reservation/<int:reservation_id>', methods=['DELETE'])(reservation_controller.delete_reservation)
app.route('/history', methods=['GET'])(order_controller.get_order_history)
app.route('/statistics', methods=['GET'])(statistics_controller.get_statistics)