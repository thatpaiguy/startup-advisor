from tools.market_tools import analyze_competition, search_trends
from utils.ollama_handler import query_ollama


def run_market_agent(startup_idea: str):
    trends = search_trends(startup_idea)
    competition = analyze_competition(startup_idea)

    prompt = f"""
You are a startup market analyst with two tools:
1. `search_trends` - shows trending news about a startup idea.
2. `analyze_competition` - shows the competitive landscape.

Here are the results from both tools:
Trends:\n{trends}
Competition:\n{competition}

Use the most relevant result above to:
- Write a short analysis of market potential. You will determine this based on anything you found from the tools.
- Score `market_demand`, `competition`, and `market_score` (1-10).
- Give an `overall_market_score` (1-10).
Respond in JSON like this without any markdown or formatting:
{{
  "analysis": "...",
  "market_demand": x,
  "competition": x,
  "market_score": x,
  "overall_market_score": x
}}
Do not return any text outside the json block output. I want only the raw json as an output. Do not put markdown ```json at ALL.
"""

    return query_ollama(prompt)
