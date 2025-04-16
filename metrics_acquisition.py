import testbed_interface as tb

def get_normalized_metrics():
    urgency = tb.get_task_urgency()
    signal = tb.get_rssi()
    link_stability = tb.get_link_stability()
    bandwidth = tb.get_bandwidth()

    U = min(urgency / 1.0, 1.0)
    S = (signal + 100) / 50
    L = link_stability
    B = min(bandwidth / 150, 1.0)

    return U, S, L, B