# main.py

from logic import detect_problem, get_risk, suggest_action

density = 25
avg_speed = 1.2
flow_status = "chaotic"
fallen = False


problem = detect_problem(density, avg_speed, flow_status, fallen)
risk = get_risk(problem)
action = suggest_action(problem)


print("Problem:", problem)
print("Risk Level:", risk)
print("Suggested Action:", action)