from common.action import Action
from common.task import Task
from common.ui import read_int, read_str

from .zipper import Zipper
from .text_analyzer import TextAnalyzer


class Task2(Task):
    name = "Task 2 (Text Analysis)"

    def actions(self):
        return super().actions() + [
            Action("Analyze file", self.analyze_file),
            Action("Zip up", self.zip_up),
            Action("Zip list", self.zip_list),
        ]

    def analyze_file(self):
        res = TextAnalyzer.from_file("test.txt")
        with open("report.txt", "w") as f:
            f.write(str(res))

        print("Report saved to report.txt")

    def zip_up(self):
        Zipper.zip_up()

        print("Archive saved to archive.zip")

    def zip_list(self):
        Zipper.zip_list()
