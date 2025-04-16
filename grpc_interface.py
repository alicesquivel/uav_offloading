import grpc
import random  # Placeholder for testing

def get_live_rssi():
    return random.uniform(-85, -60)

def get_live_bandwidth():
    return random.uniform(10, 150)

def get_live_link_stability():
    return random.uniform(0.3, 1.0)

def send_to_edge_processing(task_id, metadata=None):
    print(f"[gRPC] Sending task {task_id} to EDGE node")

def send_to_cloud_processing(task_id, metadata=None):
    print(f"[gRPC] Sending task {task_id} to CLOUD")

def send_to_local_uav(task_id):
    print(f"[gRPC] Processing task {task_id} ONBOARD")