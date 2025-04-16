import testbed_interface as tb
from offloading_engine import compute_scores
from metrics_acquisition import get_normalized_metrics

def execute_flypaw_task(task_id, weights, threshold=0.5):
    print(f"[FlyPaw] Executing task {task_id} via programmable state machine...")

    U, S, L, B = get_normalized_metrics()
    print(f"[Metrics] U={U:.2f}, S={S:.2f}, L={L:.2f}, B={B:.2f}")

    decision, score = compute_scores(U, S, L, B, weights, threshold)
    print(f"[FlyPaw] → Task {task_id} dispatched to {decision.upper()} | Score: {score}")

    tb.send_task_to_tier(task_id, decision)
    return decision