# **Day 1: LLM-Powered Customer Support Chatbot**  
🚀 **A customer support chatbot powered by Mistral 7B, SQLite, and Docker**  

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![Docker](https://img.shields.io/badge/Docker-✔-blue.svg)](https://www.docker.com/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---
![image](https://github.com/user-attachments/assets/a022fa6c-e741-48c8-8651-65149a250490)


## **📌 Features**  
✅ Uses **Mistral 7B** for natural language responses via **Ollama**  
✅ Tracks **order status** using an **SQLite database**  
✅ Runs **inside Docker** for easy deployment  
✅ Fully **integrated with GitHub**  

---

## **📌 Technologies Used**  
- 🧠 **LLM Model**: Mistral 7B (via Ollama)  
- 📂 **Database**: SQLite (stores order tracking data)  
- 🐳 **Containerization**: Docker  
- 🐍 **Language**: Python  
- 🌍 **Version Control**: Git & GitHub  

---

## **📌 Setup Instructions**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/shanojpillai/llm-chatbot.git
cd llm-chatbot
```

### **2️⃣ Install Ollama (Locally)**
If you haven't installed **Ollama**, install it using:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
For Windows, download from: [https://ollama.com](https://ollama.com)

### **3️⃣ Pull Mistral 7B**
```bash
ollama pull mistral
```

---

## **📌 Running the Chatbot (Without Docker)**
If you want to test the chatbot **without Docker**, install dependencies:  
```bash
pip install requests
```
Then, run the chatbot:
```bash
python chatbot.py
```

---

## **📌 Database Setup (SQLite)**
### **1️⃣ Create the Database**
Run this command:
```bash
python setup_db.py
```

---

## **📌 Using Docker for SQLite & Chatbot**
### **1️⃣ Build the Docker Image**
```bash
docker build -t chatbot .
```

### **2️⃣ Run Database Setup Inside Docker**
```bash
docker run --rm -v chatbot_data:/app chatbot python /app/setup_db.py
```

### **3️⃣ Run the Chatbot Inside Docker**
```bash
docker run --network host -it chatbot
```

---

## **📌 Pushing the Project to GitHub**
### **1️⃣ Initialize Git**
```bash
git init
git branch -M main
```

### **2️⃣ Link to GitHub**
```bash
git remote add origin https://github.com/shanojpillai/llm-chatbot.git
```

### **3️⃣ Add Files & Commit**
```bash
git add .
git commit -m "Initial commit: Add chatbot with SQLite and Docker"
```

### **4️⃣ Push to GitHub**
```bash
git push -u origin main
```

✅ **Now your chatbot project is on GitHub!** 🎉  

---

## **📌 Next Steps**
Now that your chatbot is fully functional, we can:  

✅ **Turn it into an API** using **FastAPI**  
✅ **Build a Web UI** using **Streamlit or React**  
✅ **Deploy the chatbot online** using **Docker Hub & GitHub Actions**  

---





---

### **📌 README Update: Day 2 - Adding a Web UI & Running Everything in Docker**  

---

# **🚀 Day 2: Adding a Web UI & Running Everything in Docker**  

Today, we **expanded our chatbot project** by adding a **fully functional Web UI using Streamlit** and integrating it with our **FastAPI-based chatbot**. We also ensured **everything runs seamlessly inside Docker**. Below is a step-by-step breakdown of what we accomplished.

---

## **📌 Steps We Accomplished Today**  

### **1️⃣ Built a Web UI for the Chatbot using Streamlit**  
- Created a new file **`web_ui.py`** to serve as the **frontend**.  
- Used **Streamlit** to create a simple UI where users can **type a question** and get a response from the chatbot.  
- Integrated an **API call to FastAPI** (`http://localhost:8000/chat`) inside the Streamlit app.  

✅ **Outcome:** Users can now interact with the chatbot using a user-friendly web interface instead of just a terminal.  



---

### **2️⃣ Updated the `Dockerfile` to Run Both FastAPI & Streamlit**  
- Installed **Streamlit** inside the Docker container.  
- Ensured that both **FastAPI (port 8000) and Streamlit (port 8501) run inside the same container**.  
- Used the following **CMD command** in `Dockerfile` to run both services:  

```dockerfile
CMD sh -c "uvicorn api:app --host 0.0.0.0 --port 8000 & sleep 5 && streamlit run web_ui.py --server.port 8501 --server.address 0.0.0.0"
```
✅ **Outcome:** Now, when the Docker container starts, both FastAPI and Streamlit launch automatically.  

---

### **3️⃣ Updated `docker-compose.yml` to Expose Both Ports**  
- Ensured **port mapping for FastAPI (`8000`) and Streamlit (`8501`)** is correctly configured.  
- Added the following lines inside `docker-compose.yml`:  

```yaml
services:
  chatbot:
    build: .
    container_name: chatbot_container
    ports:
      - "8000:8000"  # Exposing FastAPI
      - "8501:8501"  # Exposing Streamlit UI
```
✅ **Outcome:** The chatbot API and Web UI are now accessible on **`http://localhost:8000`** and **`http://localhost:8501`**, respectively.  

---

### **4️⃣ Fixed API Connection Issues Between FastAPI & Streamlit**  
- Initially, Streamlit couldn’t connect to the chatbot API due to **Docker networking issues**.  
- Updated **`web_ui.py`** to dynamically detect the API URL inside Docker:  

```python
import os
API_URL = os.getenv("API_URL", "http://localhost:8000/chat")
```
- Passed `API_URL` inside `docker-compose.yml` to **ensure connectivity**:  

```yaml
environment:
  - API_URL=http://localhost:8000/chat
```
✅ **Outcome:** Now, Streamlit correctly sends requests to FastAPI inside Docker.  

---

### **5️⃣ Rebuilt and Successfully Ran Everything in Docker**  
- Stopped any running containers:  
  ```bash
  docker-compose down
  ```
- Rebuilt everything with the latest changes:  
  ```bash
  docker-compose build --no-cache
  ```
- Started the chatbot and Web UI inside Docker:  
  ```bash
  docker-compose up
  ```
✅ **Outcome:** Everything runs inside Docker, and the chatbot is now fully functional with a web-based interface! 🎉  

---

## **📌 Final Folder Structure**
```
llm-chatbot/
├── Dockerfile             # Docker setup for FastAPI & Streamlit
├── docker-compose.yml     # Runs FastAPI + Streamlit inside Docker
├── api.py                 # FastAPI backend for chatbot API
├── web_ui.py              # Streamlit frontend for chatbot UI
├── setup_db.py            # Initializes SQLite database
├── chatbot.py             # Legacy chatbot script (now inside FastAPI)
├── requirements.txt       # Python dependencies
├── orders.db              # SQLite database (auto-created, not in Git)
└── README.md              # Documentation
```
✅ **Now, our chatbot has a user-friendly web interface and runs fully inside Docker!** 🚀  

---

## **📌 How to Run the Project**
### **1️⃣ Start the Chatbot & Web UI**
```bash
docker-compose up --build
```
✅ **FastAPI API:** **[http://localhost:8000](http://localhost:8000)**  
✅ **Streamlit Web UI:** **[http://localhost:8501](http://localhost:8501)**  

### **2️⃣ Using the Chatbot**
1️⃣ Open **[http://localhost:8501](http://localhost:8501)**  
2️⃣ Type a question (e.g., *"Where is my order?"*)  
3️⃣ Click **Send** – the chatbot will respond using **Ollama’s LLM**  

✅ **Chatbot is now fully functional with a web interface!** 🎉  

![image](https://github.com/user-attachments/assets/2de713f6-981e-4d0c-ac4e-c0cd8e998321)


---

## **📌 GitHub Commit for Today**
```bash
git add .
git commit -m "Added Streamlit Web UI & fixed API connectivity"
git push origin main
```
✅ **Now, your GitHub repo is fully updated with today's work!** 🚀  

---

### 🎯 **End of Day 2 – Fully Functional Web UI for Chatbot!**  
Now, users can **interact with the chatbot through a web-based UI**, and everything runs seamlessly inside **Docker!** 🚀🔥 

### **📌 Contributors**  
👤 **Shanoj** – *Creator & Developer*  

💡 **Feel free to contribute, submit issues, and improve the chatbot!** 🎉  

---
