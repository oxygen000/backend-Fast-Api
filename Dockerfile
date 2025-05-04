FROM python:alpine

WORKDIR /app

# Install system dependencies for face_recognition and OpenCV
RUN apk add --no-cache \
    build-base \
    cmake \
    gcc \
    g++ \
    jpeg-dev \
    python3-dev \
    musl-dev \
    openblas-dev \
    freetype-dev \
    libpng-dev \
    openblas \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    git

# Install dlib separately (dependency of face_recognition)
RUN pip install --no-cache-dir numpy
RUN git clone -b 'v19.21' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd dlib/ && \
    python setup.py install --no USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA && \
    cd .. && \
    rm -rf dlib/

# Copy requirements first for better caching
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p data logs uploads

# Set environment variables
ENV API_HOST=0.0.0.0
ENV API_PORT=8000
ENV API_DEBUG=False
ENV LOG_LEVEL=INFO

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]

