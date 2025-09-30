# Use the official Python 3.11 slim image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user with UID 1000 named "appuser"
RUN useradd -m -u 1000 appuser

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY main.py .

# Switch to the non-root user for security
USER appuser

# Set the APP_PORT environment variable required by the task
ENV APP_PORT=7473

# Expose the port the app will run on
EXPOSE 7473

# The command to run the application using uvicorn
# --host 0.0.0.0 is essential for the container to be accessible from outside
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7473"]