import matplotlib.pyplot as plt
import pandas as pd

from half_life.half_life import run_experiment


def main():
    results = []
    for _ in range(5):
        results.append(run_experiment(nr_of_dice=20, nr_throws=10))

    df = pd.DataFrame(results)
    plt.plot(df.sum())
    plt.show()
