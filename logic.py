
def detect_problem(density, avg_speed, flow_status, fallen):

    if fallen:
        return "FALL_DETECTED"
    
    if density > 20 and avg_speed < 2:
        return "BOTTLENECK"
    
    if flow_status == "chaotic":
        return "FLOW_CONFLICT"
    
    if avg_speed < 1:
        return "SLOWDOWN"
    
    return "NORMAL"


def get_risk(problem):

    if problem == "NORMAL":
        return "LOW"
    
    if problem in ["SLOWDOWN", "FLOW_CONFLICT"]:
        return "MEDIUM"
    
    if problem in ["BOTTLENECK", "FALL_DETECTED"]:
        return "HIGH"


def suggest_action(problem):

    if problem == "BOTTLENECK":
        return "Open additional gates"
    
    if problem == "FLOW_CONFLICT":
        return "Stop entry temporarily"
    
    if problem == "SLOWDOWN":
        return "Redirect crowd to less dense or empty zones"
    
    if problem == "FALL_DETECTED":
        return "Alert emergency response immediately"
    
    return "No action needed"