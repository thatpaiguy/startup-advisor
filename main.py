from agents.orchestrator_agent import orchestrate
from utils.logger import print_to_console_also

def main():
    print_to_console_also("🚀 Startup Advisor System")
    print_to_console_also("Describe your startup idea:\n> ")
    idea = input()
    print_to_console_also("\n🔎 Analyzing...\n")

    result = orchestrate(idea)
    print_to_console_also("\n✅ Final Recommendation:\n")
    print_to_console_also(result)

if __name__ == "__main__":
    main()
