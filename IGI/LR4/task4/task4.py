from common.action import Action
from common.task import Task
from common.ui import read_float, read_int, read_str

from .shape_color import ShapeColor
from .parallelogram import Parallelogram

import math


class Task4(Task):
    name = "Task 4 (Parallelogram)"

    def __init__(self):
        super().__init__()

        d1_val = read_float("Enter first diagonal: ", min=0.0001)
        d2_val = read_float("Enter second diagonal: ", min=0.0001)
        angle_val = read_float("Enter angle: ", min=-math.pi, max=math.pi)
        color_val = read_str("Enter color: ")

        self.shape_title = read_str("Enter shape title: ")
        self.shape = Parallelogram(d1_val, d2_val, angle_val, ShapeColor(color_val))

    def menu_text(self):
        return f"{self.shape}\nArea: {self.shape.area():.3f}"

    def actions(self):
        return super().actions() + [
            # Action("Show math values", self.show_values),
            Action("Plot shape", self.show_graph),
            Action("Save shape", self.save_graph),
        ]

    def show_graph(self):
        self.plot_graph("show")

    def save_graph(self):
        self.plot_graph("save")

    def plot_graph(self, show_or_save="show"):
        import matplotlib.pyplot as plt

        points = self.shape.points()
        plt.fill(
            [pp[0] for pp in points],
            [pp[1] for pp in points],
            facecolor=self.shape.color.color,
        )
        plt.gca().set_aspect("equal")
        plt.title(self.shape_title)

        if show_or_save == "show":
            plt.show()
        else:
            plt.savefig("4.png")
