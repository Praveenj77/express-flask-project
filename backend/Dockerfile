FROM python:3.9-alpine

WORKDIR /app

# Install system dependencies for pip packages
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Set environment variables for Flask (optional but helpful)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python3", "-u", "app.py"]
