# AERPAW UAV Task Offloading Framework

This repository provides a complete, testbed-ready UAV offloading simulation and deployment system for **AERPAW**. It includes support for:

- Multi-metric offloading engine (urgency, RSSI, bandwidth, link stability)
- Integration-ready **gRPC APIs** for telemetry + control
- Plotting utilities for analyzing offloading decisions
- Docker support for local or AERPAW-based deployment

---

## Project Structure

```
.
├── main.py                 # Entry point for basic offloading test
├── batch_simulation.py     # Batch testing for 30 UAV tasks
├── flypaw_integration.py   # Integrates with FlyPaw programmable missions
├── plot_results.py         # Visualization of simulation output
├── grpc_interface.py       # Mocked gRPC hooks for live telemetry
├── protos/                 # .proto files for telemetry + control
├── Dockerfile              # Container for sim/testbed execution
├── requirements.txt        # Python dependencies
```

---

## Running in Docker

To simulate offloading tasks in a container:

```bash
docker build -t aerpaw-uav .
docker run --rm aerpaw-uav
```

---

## AERPAW Integration

To integrate with AERPAW:

1. Compile `.proto` files:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/*.proto
```

2. Replace mocked methods in `grpc_interface.py` with real AERPAW gRPC service clients.

3. Use `flypaw_integration.py` in your programmable mission to control UAV offloading via FlyPaw states.

---

## Plotting Results

After running batch simulations:

```bash
python batch_simulation.py
python plot_results.py
```

---

## Output Logs

- `results_log.json` – stores task decisions and scores for plotting and export.

---
