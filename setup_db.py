import sqlite3

# Store the database inside Docker at /app/orders.db
DB_PATH = "/app/orders.db"

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create the orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    status TEXT
)
""")

# Insert some sample data
orders = [
    ("12345", "Shipped - Expected delivery: Feb 28, 2025"),
    ("67890", "Processing - Your order is being prepared."),
    ("11121", "Delivered - Your package was delivered on Feb 20, 2025."),
]
cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?)", orders)

# Save changes and close
conn.commit()
conn.close()

print("✅ Database setup complete inside Docker!")
