FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for face_recognition
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data logs uploads && chmod -R 777 data logs uploads

# Set environment variables
ENV API_HOST=0.0.0.0
ENV API_PORT=8000
ENV API_DEBUG=False
ENV LOG_LEVEL=INFO

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]


