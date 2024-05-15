from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config.Config')  # Load configuration from config.py

# Initialize database
db = MySQL(app)

# Import and register blueprints
from routes.menu_routes import menu_blueprint
app.register_blueprint(menu_blueprint, url_prefix='/menu')

from routes.reservation_routes import reservation_blueprint
app.register_blueprint(reservation_blueprint, url_prefix='/reservations')

from routes.order_routes import order_blueprint
app.register_blueprint(order_blueprint, url_prefix='/orders')

from routes.feedback_routes import feedback_blueprint
app.register_blueprint(feedback_blueprint, url_prefix='/feedbacks')
