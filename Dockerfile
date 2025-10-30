# Dockerfile

# Use a lightweight official Python image
FROM python:3.10-slim

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT 8501
EXPOSE 8501

# Set the working directory
WORKDIR /app

# Copy requirements and install packages first (for better caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Command to run the Streamlit application
# Note: Streamlit needs to bind to 0.0.0.0 for Azure networking
CMD ["streamlit", "run", "webapp.py", "--server.port=8501", "--server.address=0.0.0.0"]