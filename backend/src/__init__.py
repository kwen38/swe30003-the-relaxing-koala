from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Connect to MySql
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@",
    database="koala_cafe"
)

# Import and register blueprints
from controllers.menu_routes import menu_blueprint
app.register_blueprint(menu_blueprint, url_prefix='/menu')

from controllers.reservation_routes import reservation_blueprint
app.register_blueprint(reservation_blueprint, url_prefix='/reservations')

from controllers.order_routes import order_blueprint
app.register_blueprint(order_blueprint, url_prefix='/orders')

from controllers.feedback_routes import feedback_blueprint
app.register_blueprint(feedback_blueprint, url_prefix='/feedbacks')
