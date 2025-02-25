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

### **📜 License**
This project is licensed under the **MIT License**.  

👉 **Want to improve the chatbot? Fork the repo and contribute!** 🚀😊  

---

### **📌 Contributors**  
👤 **Shanoj** – *Creator & Developer*  

💡 **Feel free to contribute, submit issues, and improve the chatbot!** 🎉  

---
