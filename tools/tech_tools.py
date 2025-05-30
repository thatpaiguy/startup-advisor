import requests

def suggest_stack(idea: str) -> str:
    """Suggests a tech stack based on the startup idea using a ruleset."""
    
    if "AI" in idea:
        stack = "Python, FastAPI, PyTorch, PostgreSQL"
    if "ecommerce" in idea:
        stack = "React, Node.js, MongoDB"
    else:
        stack = "React, Flask, SQLite"
    print("Suggested stack: " , stack, "\n")
    return stack

def estimate_dev_time(features: list[str]) -> str:
    """Estimates development time based on the number of features."""
    base_weeks = 2
    time = base_weeks + len(features) * 1.5
    dev_time = f"{time:.1f} weeks"
    print("Estimate development time: ", dev_time, "\n")
    return dev_time
