# Startup Advisor Multi-Agent System

This project uses multiple AI agents (Market + Technical + Orchestrator) to evaluate startup ideas using real-world tools and a local LLM (Gemma 2B via Ollama).

## Requirements

- Python 3.9+
- Docker + Docker Compose
- [NewsAPI](https://newsapi.org/) Key

## Setup
Ensure Docker is running.
```bash
# Clone the repo
git clone https://github.com/yourname/startup-advisor.git
cd startup-advisor

# Install Python deps
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Set your NewsAPI key
cp .env.example .env
# Then edit .env and insert your key

# Start Ollama with Gemma 2B
docker compose -f docker-compose.yml up
# Close this terminal process when `ollama-1  | success` is displayed, otherwise you will see docker logs

# Run the app
python3 main.py
