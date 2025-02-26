import requests
import sqlite3
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load Ollama host from environment variable (for Docker networking)
import os
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")  # ✅ Use localhost
OLLAMA_URL = f"{OLLAMA_HOST}/api/generate"

# Initialize FastAPI app
app = FastAPI()

# Database path inside Docker
DB_PATH = "/app/orders.db"

# Define request model for chatbot input
class ChatRequest(BaseModel):
    message: str

# Function to fetch order status
def get_order_status(order_id):
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=500, detail="Database file not found!")

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if orders table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders';")
        if not cursor.fetchone():
            conn.close()
            raise HTTPException(status_code=500, detail="Orders table does not exist!")

        # Fetch order status
        cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return {"order_id": order_id, "status": result[0]}
        else:
            raise HTTPException(status_code=404, detail="Order not found!")

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# API Endpoint: Chat with the chatbot (expects JSON input)
@app.post("/chat")
def chat_with_bot(request: ChatRequest):
    data = {"model": "mistral", "prompt": request.message, "stream": False}

    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()  # Raise an error if the request fails

        return {"response": response.json()["response"]}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")

# API Endpoint: Get order status
@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return get_order_status(order_id)

# Run with: uvicorn api:app --host 0.0.0.0 --port 8000
