import sqlite3

# Path to the database inside Docker
DB_PATH = "/app/orders.db"

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Query the orders table
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

# Print the results
for order in orders:
    print(f"Order ID: {order[0]}, Status: {order[1]}")

# Close the connection
conn.close()