import requests

url = "http://localhost:11434/api/generate"

print("Welcome to the Customer Support Chatbot! Type 'exit' to stop.\n")

# System instruction to make the chatbot act like a real agent
system_prompt = """
You are a customer support assistant for an online shopping company. 
Your job is to help customers with order tracking, returns, and product details. 
Always be polite and provide helpful answers.
"""

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    data = {
        "model": "mistral",
        "prompt": f"{system_prompt}\nCustomer: {user_input}\nAgent:",
        "stream": False
    }

    response = requests.post(url, json=data)
    print("Chatbot:", response.json()["response"])
# Output:
# Welcome to the Customer Support Chatbot! Type 'exit' to stop.