import matplotlib.pyplot as plt
import numpy as np

def generate_cycle_graph():
    days = np.arange(1, 29)
    hormone_levels = np.sin(np.linspace(0, 3 * np.pi, 28)) * 20 + 50

    fig, ax = plt.subplots()
    ax.plot(days, hormone_levels, linewidth=3)
    ax.set_title("Menstrual Cycle Hormone Variation")
    ax.set_xlabel("Cycle Day")
    ax.set_ylabel("Hormone Level")
    ax.grid(True)

    return fig
