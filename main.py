from metrics_acquisition import get_normalized_metrics
from offloading_engine import compute_scores
from task_profiles import TASKS
import testbed_interface as tb
import time

threshold = 0.5

for task in TASKS:
    task_id = task["id"]
    weights = task["weights"]
    print(f"\n--- Processing {task_id} ---")
    
    U, S, L, B = get_normalized_metrics()
    print(f"[Metrics] Urgency: {U:.2f}, Signal: {S:.2f}, Link: {L:.2f}, Bandwidth: {B:.2f}")
    
    decision, score = compute_scores(U, S, L, B, weights, threshold)
    print(f"[Decision] → Offload to: {decision.upper()} | Score: {score}")

    tb.send_task_to_tier(task_id, decision)
    time.sleep(1)