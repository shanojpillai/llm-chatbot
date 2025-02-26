# Use an official Python image
FROM python:3.10

# Install SQLite inside the container
RUN apt-get update && apt-get install -y sqlite3

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages
RUN pip install requests fastapi uvicorn streamlit

# Ensure the database is set up before running the API
RUN python /app/setup_db.py  # ✅ Ensures database setup

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Start FastAPI & Streamlit
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run web_ui.py --server.port 8501 --server.address 0.0.0.0"]
