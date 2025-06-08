import sqlite3

def verify_id(id_number):
    # Connect to the database
    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    # Query the user by ID number
    cursor.execute("SELECT * FROM users WHERE id_number = ?", (id_number,))
    result = cursor.fetchone()

    conn.close()

    if result:
        # Found the user, return the data as a dictionary
        keys = ["full_name", "id_number", "email", "nationality", "address"]
        user_data = dict(zip(keys, result))
        return user_data
    else:
        # User not found
        return None
