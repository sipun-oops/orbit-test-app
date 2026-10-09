# Use the official lightweight Python image.
FROM python:3.11-slim AS base

# Set environment variables for Python.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install OS-level dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libpq-dev \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user and switch to it.
RUN useradd -m appuser
WORKDIR /app
COPY --chown=appuser:appuser requirements.txt .

# Install Python dependencies.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application source code.
COPY --chown=appuser:appuser . .

# Switch to non-root user.
USER appuser

# Expose the port the app runs on.
EXPOSE 8080

# Use gunicorn as the production WSGI server.
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
