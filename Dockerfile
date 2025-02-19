# Use a smaller base image
FROM python:3.9-slim

# Install Chromium and Chromium Driver
RUN apt-get update && apt-get install -y chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY your_script.py .

# Run the script
CMD ["python", "your_script.py"]
