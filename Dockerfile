FROM python:3.10-slim

# Set working directory
WORKDIR /deploy

# Copy core application files
COPY app/main.py /deploy/
COPY app/config.yaml /deploy/
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    libglib2.0-0 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase (e.g., waste_image_recognition, assets, etc.)
COPY . .

# Expose the FastAPI port
EXPOSE 8080

# Use CMD instead of ENTRYPOINT for flexibility (see notes below)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
