import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def search_trends(idea: str) -> str:
    """Searches recent news trends related to the startup idea."""
    url = f"https://newsapi.org/v2/everything?q={idea}&sortBy=popularity&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Could not fetch trend data."
    articles = response.json().get("articles", [])
    news_api_response = "\n".join([a["title"] for a in articles[:3]])
    print("News API Response: ", news_api_response, "\n")
    return news_api_response

def analyze_competition(idea: str) -> str:
    """Analyzes competition using a simple web search (placeholder logic)."""
    analysis = f"Top competitors for '{idea}' include Company A and Company B"
    print("Competition Analysis: ", analysis, "\n")
    return analysis