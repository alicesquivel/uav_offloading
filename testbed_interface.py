import random

def get_rssi():
    return random.uniform(-85, -55)

def get_bandwidth():
    return random.uniform(10, 100)

def get_link_stability():
    return random.uniform(0.3, 1.0)

def get_task_urgency():
    return random.uniform(0.3, 1.0)

def send_task_to_tier(task_id, tier):
    print(f"[AERPAW] Task {task_id} dispatched to {tier.upper()} node.")