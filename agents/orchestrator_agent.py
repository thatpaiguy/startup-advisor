import json

from agents.market_agent import run_market_agent
from agents.tech_agent import run_tech_agent
from utils.ollama_handler import query_ollama

def orchestrate(startup_idea: str):
    # Get agent outputs
    market_response = run_market_agent(startup_idea)
    print("Market Response: ", market_response, "\n")
    tech_response = run_tech_agent(startup_idea)
    print("Tech Response: ", tech_response, "\n")

    try:
        market_data = json.loads(market_response)
        tech_data = json.loads(tech_response)
    except json.JSONDecodeError:
        raise ValueError("Agent response was not valid JSON. Check agent formatting or LLM response.")

    # Prepare summary prompt
    prompt = f"""
You are a startup advisor.
Here is my idea: {startup_idea}
Here is the Market Agent analysis:
Analysis: {market_data['analysis']} (This comes from a news api so make sure you consider that it may not be related to the original startup idea.)
Scores:
- Market Demand: {market_data['market_demand']}
- Competition: {market_data['competition']}
- Market Score: {market_data['market_score']}
- Overall Market Score: {market_data['overall_market_score']}

Here is the Tech Agent analysis:
Analysis: {tech_data['analysis']}
Scores:
- Tech Stack: {tech_data['tech_stack']}
- Estimated Dev Time Weeks: {tech_data['estimated_dev_time_weeks']}
- Tech Score: {tech_data['tech_score']}
- Overall Tech Feasibility: {tech_data['overall_tech_feasibility']}

Using this, write a summary combining both perspectives. Make a recommendation on whether the startup idea should be pursued. Explain clearly using the scores and analysis.
Respond in plain text.
"""

    return query_ollama(prompt)