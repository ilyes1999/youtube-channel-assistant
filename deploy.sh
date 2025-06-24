#!/bin/bash

# Content Creation Agency Deployment Script

set -e

echo "🚀 Starting Content Creation Agency deployment..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your API keys:"
    echo "cp env.production.template .env"
    echo "Then edit .env with your actual API keys"
    exit 1
fi

# Create logs directory
mkdir -p logs

# Build and start with Docker Compose
echo "📦 Building and starting services..."
docker-compose up --build -d

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check if the application is running
if curl -f http://localhost:7860/ > /dev/null 2>&1; then
    echo "✅ Content Creation Agency is running successfully!"
    echo "🌐 Access the application at: http://localhost:7860"
    echo "📊 View logs with: docker-compose logs -f"
else
    echo "❌ Application failed to start. Check logs:"
    docker-compose logs
    exit 1
fi

echo "🎉 Deployment completed successfully!" 