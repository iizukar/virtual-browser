# Use the official Python 3.9 image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y wget gnupg2 unzip \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/133.0.6943.126/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip -d /usr/local/bin/ \
    && rm chromedriver-linux64.zip \
    && chmod +x /usr/local/bin/chromedriver-linux64/chromedriver

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
