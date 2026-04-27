# import math
import math
from common.action import Action
from common.task import Task
from common.ui import read_float, read_int, read_str

import numpy as np


class Task5(Task):
    name = "Task 5"

    def __init__(self):
        super().__init__()

        self.arr = np.random.randint(-100, 100, (8, 8))
        print(self.arr)

        self.show_base_a()
        self.show_base_b()

        self.show_main()

    def show_base_a(self):
        print("Zeros: ", np.zeros((2, 3)))
        print("Ones: ", np.ones((3, 2)))
        print("Eye:", np.eye(3))
        print("Indexing: ", self.arr[2:5:2, 2:5:2])
        print("Add 8 to al: ", self.arr + 8)

    def show_base_b(self):
        print("Mean: ", np.mean(self.arr))
        print("Median: ", np.median(self.arr))
        print("Corr matr:", np.corrcoef(self.arr))
        print("Variance: ", np.var(self.arr))
        print("Std: ", np.std(self.arr))

    def show_main(self):
        stage1 = self.arr
        stage1 = np.abs(stage1[stage1 < 0])
        print(stage1)
        stage1 = stage1[stage1 % 2 == 1]

        print("Stage 1: ", np.sum(stage1))
        print("Stage 2: ", np.std(stage1))

        mean = np.mean(stage1)
        half_dev = np.sum((stage1 - mean) ** 2)
        print("Stage 2 man: ", math.sqrt(half_dev / stage1.size))


if __name__ == "__main__":
    Task5()
