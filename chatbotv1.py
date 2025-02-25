import requests

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

print("Welcome to the Customer Support Chatbot! Type 'exit' to stop.\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    # API request data
    data = {
        "model": "mistral",
        "prompt": user_input,
        "stream": False
    }

    # Send request to Ollama API
    response = requests.post(url, json=data)

    # Print chatbot response
    print("Chatbot:", response.json()["response"])
