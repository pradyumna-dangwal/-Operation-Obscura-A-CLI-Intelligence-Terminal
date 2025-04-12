from agent.generator import create_agent
from mission.log_simulator import simulate_logs
from utils.terminal_effects import glitch_text

print(glitch_text("Welcome to Operation Obscura"))
create_agent()
simulate_logs()