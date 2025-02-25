# LLM Chatbot using Mistral & Ollama (Docker)

This project runs a local chatbot using **Mistral 7B** inside **Docker** with **Ollama**.

## 🔧 Setup

1️⃣ **Run Ollama in Docker**
```bash
docker run -d --name ollama -p 11434:11434 ollama/ollama
docker exec -it ollama ollama pull mistral
