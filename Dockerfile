# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libboost-all-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    python3-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file
COPY requirements.txt .

# Install dlib separately first
RUN pip install --no-cache-dir dlib==19.22.1

# Install Python packages
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

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
