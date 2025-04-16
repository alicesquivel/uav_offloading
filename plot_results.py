import matplotlib.pyplot as plt
import pandas as pd
import json

def load_results(filepath="results_log.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def plot_offloading_distribution(df):
    counts = df['tier'].value_counts()
    counts.plot(kind='bar', color='skyblue')
    plt.title("Offloading Decisions by Tier")
    plt.ylabel("Number of Tasks")
    plt.xlabel("Execution Tier")
    plt.tight_layout()
    plt.show()

def plot_metric_scores(df):
    plt.scatter(df['score'], df['B'], label='Bandwidth', alpha=0.7)
    plt.scatter(df['score'], df['S'], label='Signal Strength', alpha=0.7)
    plt.xlabel("Score")
    plt.ylabel("Metric Value")
    plt.title("Score vs. Metrics")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_results()
    plot_offloading_distribution(df)
    plot_metric_scores(df)