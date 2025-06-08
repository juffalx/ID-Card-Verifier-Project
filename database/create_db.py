import sqlite3

# Step 1: Connect to SQLite (will create users.db if it doesn't exist)
conn = sqlite3.connect("database/users.db")

# Step 2: Create a cursor to execute SQL commands
cursor = conn.cursor()

# Step 3: Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    full_name TEXT,
    id_number TEXT PRIMARY KEY,
    email TEXT,
    nationality TEXT,
    address TEXT
)
""")

# Step 4: Insert sample data
cursor.execute("""
INSERT OR IGNORE INTO users (full_name, id_number, email, nationality, address)
VALUES (?, ?, ?, ?, ?)
""", (
    "JOHN DOE",
    "JB-007",
    "john@example.com",
    "AMERICAN",
    "123 MAIN STREET, YOUR CITY, USA 789456"
))

# Step 5: Commit and close connection
conn.commit()
conn.close()

print("✅ Database and table created with sample data.")
