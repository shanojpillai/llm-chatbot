import requests

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Fake database: Order ID → Status
orders_db = {
    "12345": "Shipped - Expected delivery: Feb 28, 2025",
    "67890": "Processing - Your order is being prepared.",
    "11121": "Delivered - Your package was delivered on Feb 20, 2025.",
}

# System message: Makes the chatbot act like a real support agent
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

    # Check if user provided an order number
    if any(order_id in user_input for order_id in orders_db.keys()):
        order_id = next(order_id for order_id in orders_db.keys() if order_id in user_input)
        chatbot_response = f"Order {order_id} Status: {orders_db[order_id]}"
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
