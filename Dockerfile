# Start from a small official Python image
FROM python:3.12-slim

WORKDIR /app

# Install libraries first (Docker caches this step)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

EXPOSE 8080

# Gunicorn is the production server (Flask's built-in one is for development only)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
