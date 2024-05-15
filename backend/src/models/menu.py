from flask import current_app as app

def create_menu_table():
    cursor = app.mysql.connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INT AUTO_INCREMENT PRIMARY KEY,
            items TEXT
        )
    """)
    app.mysql.connection.commit()
    cursor.close()

def get_menu():
    cursor = app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    cursor.close()
    return items
