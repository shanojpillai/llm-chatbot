# Use an official Python image
FROM python:3.10

# Install SQLite inside the container
RUN apt-get update && apt-get install -y sqlite3

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install required Python packages
RUN pip install requests

# Expose port (optional, if we later add an API)
EXPOSE 5000

# Run the chatbot script
CMD ["python", "chatbot.py"]

RUN python setup_db.py
