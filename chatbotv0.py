import requests

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Prompt for the chatbot
data = {
    "model": "mistral",  # Use the Mistral 7B model
    "prompt": "Where is my order?",  # User input message
    "stream": False  # Get the full response at once
}

# Send the request to the local Ollama instance
response = requests.post(url, json=data)

# Print the response
print("Chatbot Response:", response.json()["response"])
