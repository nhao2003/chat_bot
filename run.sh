#!/bin/bash

# Exit immediately if any command fails
set -e

# Build Docker image
echo "Building Docker image..."
docker build -t chat_bot .

# Run Docker container
echo "Starting Docker container..."
docker run -d -p 5000:5000 chat_bot

echo "Docker container started successfully."
