from flask import current_app as app

def get_menu():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    cursor.close()
    return items
