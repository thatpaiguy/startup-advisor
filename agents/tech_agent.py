from tools.tech_tools import estimate_dev_time, suggest_stack
from utils.ollama_handler import query_ollama


def run_tech_agent(startup_idea: str):
    stack = suggest_stack(startup_idea)
    time = estimate_dev_time(["AI chatbot", "real-time video feedback", "dashboard"])

    prompt = f"""
You are a technical advisor with two tools:
1. `suggest_stack` - suggests a tech stack.
2. `estimate_dev_time` - estimates time to develop features.

Here are the results:
Tech Stack:\n{stack}
Dev Time Estimate:\n{time}

Use the most relevant result above to:
- Write a short technical feasibility paragraph. You will determine this based on anything you found from the tools.
- Score `tech_stack`, `estimated_dev_time_weeks`, and `tech_score` (1-10).
- Give an `overall_tech_feasibility` (1-10).
Respond in JSON like this without any markdown or formatting:
{{
  "analysis": "...",
  "tech_stack": x,
  "estimated_dev_time_weeks": x,
  "tech_score": x,
  "overall_tech_feasibility": x
}}

Do not return any text outside the json block output. I want only the raw json as an output. Do not put markdown ```json at ALL. 
"""

    return query_ollama(prompt)
