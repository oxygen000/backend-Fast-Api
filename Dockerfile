# استخدم نسخة مناسبة وثابتة من Python
FROM python:3.12-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# تثبيت المتطلبات الأساسية التي تحتاجها مكتبة face_recognition و dlib
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

# نسخ ملف المتطلبات أولاً لتقليل الطبقات في كل مرة
COPY requirements.txt .

# تثبيت مكتبات بايثون المطلوبة
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# نسخ كود المشروع
COPY . .

# إنشاء المجلدات الضرورية وتعيين التصاريح
RUN mkdir -p data logs uploads && chmod -R 777 data logs uploads

# تعيين متغيرات البيئة
ENV API_HOST=0.0.0.0
ENV API_PORT=8000
ENV API_DEBUG=False
ENV LOG_LEVEL=INFO

# فتح المنفذ
EXPOSE 8000

# أمر التشغيل الأساسي
CMD ["python", "main.py"]
