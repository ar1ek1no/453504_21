import math
from common.action import Action
from common.task import Task
from common.ui import read_float, read_int, read_str
import matplotlib.pyplot as plt
from task3.row import emit_full_row

from statistics import mean, median, mode, pvariance, stdev

NANO_EPS = 1e-9


class Task3(Task):
    name = "Task 3 (Math & Plotting)"

    def __init__(self):
        super().__init__()

        self.x_val = read_float(
            "Enter x (-inf to -1) or (1 to inf): ",
            ranges=[(-math.inf, -1 - NANO_EPS), (1 + NANO_EPS, math.inf)],
        )
        self.f_val = math.log((self.x_val + 1) / (self.x_val - 1))
        self.row = list(emit_full_row(self.x_val, 1e-5, self.f_val))

    def actions(self):
        return super().actions() + [
            Action("Show math values", self.show_values),
            Action("Plot graph", self.plot_graph),
        ]

    def show_values(self):
        row_e = [row[3] for row in self.row]
        print(f"\n--- Statistical Parameters ---")
        print(f"Mean: {mean(row_e)}")
        print(f"Median: {median(row_e)}")
        print(f"Mode: {mode(row_e)}")
        print(f"Variance: {pvariance(row_e)}")
        print(f"Standard deviation: {stdev(row_e)}")

        avg_err = mean([row[4] * row[4] for row in self.row])
        print(f"Average absolute error: {avg_err}")

    def plot_graph(self):
        iterations = [r[1] for r in self.row]
        approx_values = [r[3] for r in self.row]
        target_values = [r[2] for r in self.row]

        plt.figure(figsize=(10, 6))
        plt.plot(iterations, target_values, 'r--', label="Math F(x) (target)")
        plt.plot(iterations, approx_values, 'b-o', label="Series Sum (approx)")

        plt.xlabel("Number of iterations (n)")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.title(f"Convergence of ln((x+1)/(x-1)) for x={self.x_val}")

        plt.savefig("plot.png")
        print("Graph saved to plot.png")
        plt.show()
