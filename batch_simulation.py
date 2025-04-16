from task_profiles import TASKS
from offloading_engine import compute_scores
from metrics_acquisition import get_normalized_metrics
import testbed_interface as tb
import time
import json

def simulate_batch(n=30, threshold=0.5):
    results = []
    for i in range(n):
        task = TASKS[i % len(TASKS)]
        task_id = f"{task['id']}_{i}"
        weights = task["weights"]
        U, S, L, B = get_normalized_metrics()
        decision, score = compute_scores(U, S, L, B, weights, threshold)
        tb.send_task_to_tier(task_id, decision)
        results.append({
            "task": task_id,
            "tier": decision,
            "score": round(score, 3),
            "U": round(U, 2), "S": round(S, 2), "L": round(L, 2), "B": round(B, 2)
        })
        time.sleep(0.2)
    return results

if __name__ == "__main__":
    res = simulate_batch()
    with open("results_log.json", "w") as f:
        json.dump(res, f, indent=2)
    for r in res:
        print(r)