# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY content_creation_agency/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY content_creation_agency/ ./content_creation_agency/
COPY setup.py .

# Install the package in development mode
RUN pip install -e .

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Expose port
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Run the application
CMD ["python", "content_creation_agency/production_app.py"] 