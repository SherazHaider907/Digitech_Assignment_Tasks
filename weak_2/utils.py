def validate_priority(priority):
    return priority in ["Low", "Medium", "High"]

def get_valid_priority():
    while True:
        p = input("Enter priority (Low/Medium/High): ")
        if validate_priority(p):
            return p
        print("Invalid priority!")

def get_int_input(prompt):
    try:
        return int(input(prompt))
    except:
        return None