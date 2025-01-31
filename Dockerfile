# Use Python base image
FROM python:3.9  

# Set working directory
WORKDIR /app  

# Copy all project files
COPY . .  

# Install dependencies
RUN pip install -r requirements.txt  

# Expose the Streamlit port
EXPOSE 8501  

# Command to run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
