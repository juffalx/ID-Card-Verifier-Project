       
import sqlite3

# Connect to the database
conn = sqlite3.connect("database/users.db")
cursor = conn.cursor()

# Simulated OCR result (in practice, extract these from your OCR result)
ocr_id = "JB-007".upper().strip()

# Search by ID number (recommended, as it's unique)
cursor.execute("SELECT * FROM users WHERE id_number = ?", (ocr_id,))
result = cursor.fetchone()

# Print result
if result:
    print("✅ Match Found in Database:")
    print(f"Name: {result[0]}")
    print(f"ID Number: {result[1]}")
    print(f"Email: {result[2]}")
    print(f"Nationality: {result[3]}")
    print(f"Address: {result[4]}")
else:
    print("❌ No match found for ID:", ocr_id)

conn.close()
