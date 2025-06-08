import easyocr
import sqlite3

def auto_verify_from_image(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    text_results = reader.readtext(image_path, detail=0)
    
    combined_text = ' '.join(text_results).upper()
    possible_ids = [word for word in combined_text.split() if '-' in word]
    if not possible_ids:
        return None
    
    id_number = possible_ids[0].strip()
    
    conn = sqlite3.connect("../database/users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id_number = ?", (id_number,))
    user = cursor.fetchone()
    conn.close()

    if user:
        keys = ["full_name", "id_number", "email", "nationality", "address"]
        return dict(zip(keys, user))
    else:
        return None
