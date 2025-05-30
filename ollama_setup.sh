#!/bin/bash

# Pull Gemma if not pulled
docker pull ollama/ollama

# Start Ollama container so it can download the model
docker-compose up -d ollama

# Give Ollama some time to start
sleep 10

# Pull the model
curl http://localhost:11434/api/pull -d '{"name": "gemma:2b"}'

echo "Ollama setup complete. Run 'docker-compose up --build' to start the full app."
