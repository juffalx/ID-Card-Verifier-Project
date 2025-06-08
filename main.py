from db_module import verify_id

# Suppose you extracted this ID from OCR:
extracted_id = "JB-007"

user = verify_id(extracted_id)
if user:
    print("User found:", user)
else:
    print("User not found.")
