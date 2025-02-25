import requests
import sqlite3
import os

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Explicitly set the correct database path inside Docker
DB_PATH = "/app/orders.db"

# Function to fetch order status from SQLite
def get_order_status(order_id):
    # Ensure the database file exists before trying to connect
    if not os.path.exists(DB_PATH):
        return "Error: Database file not found! Please ensure the database is initialized."

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Check if the orders table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders';")
    table_exists = cursor.fetchone()
    if not table_exists:
        conn.close()
        return "Error: Orders table does not exist!"

    cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
    result = cursor.fetchone()
    conn.close()

    return result[0] if result else "Sorry, I couldn't find that order."

# System instruction for chatbot
system_prompt = """
You are a customer support assistant for an online shopping company. 
Your job is to help customers with order tracking, returns, and product details. 
Always be polite and provide helpful answers.
If the user asks about an order, ask them for their order number.
"""

print("Welcome to the Customer Support Chatbot! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    # Check if the user provided an order number (5-digit number)
    words = user_input.split()
    order_id = next((word for word in words if word.isdigit() and len(word) == 5), None)

    if order_id:
        chatbot_response = f"Order {order_id} Status: {get_order_status(order_id)}"
    else:
        # Send the question to Mistral for a response
        data = {
            "model": "mistral",
            "prompt": f"{system_prompt}\nCustomer: {user_input}\nAgent:",
            "stream": False
        }

        response = requests.post(url, json=data)
        chatbot_response = response.json()["response"]

    print("Chatbot:", chatbot_response)
