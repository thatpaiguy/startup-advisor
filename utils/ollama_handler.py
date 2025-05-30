import requests


def query_ollama(prompt):
        payload = {
            "model": "gemma:2b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }

        response = requests.post("http://localhost:11434/api/chat", json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"]