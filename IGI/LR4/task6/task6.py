import pandas as pd
from common.action import Action
from common.task import Task

class Task6(Task):
    name = "Task 6 (Pandas Weather Analysis)"

    def __init__(self):
        super().__init__()
        try:
            self.df = pd.read_csv("weatherHistory.csv")
        except FileNotFoundError:
            print("Error: weatherHistory.csv not found!")
            self.df = None

    def actions(self):
        return super().actions() + [
            Action("Show Task A (First 7 days Temperature/Humidity)", self.task_a),
            Action("Show Task B (Temperature Decile Analysis)", self.task_b),
            Action("Show DataFrame Stats", self.show_info),
        ]

    def show_info(self):
        if self.df is not None:
            print("\n--- Dataset Info ---")
            print(self.df.info())

    def task_a(self):
        if self.df is not None:
            # Selecting first 7 rows and specific columns: Temperature (C) and Humidity
            subset = self.df.iloc[:7][['Temperature (C)', 'Humidity']].copy()
            weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            subset.index = weekdays

            print("\n--- First 7 Days (Temp & Humidity) ---")
            print(subset)

    def task_b(self):
        """Calculates ratio between the hottest decile and coldest decile"""
        if self.df is not None:
            temp_col = 'Temperature (C)'

            # Calculating deciles
            upper_decile_threshold = self.df[temp_col].quantile(0.9)
            lower_decile_threshold = self.df[temp_col].quantile(0.1)

            # Mean of top 10% hottest days
            mean_hottest = self.df[self.df[temp_col] >= upper_decile_threshold][temp_col].mean()
            # Mean of bottom 10% coldest days
            mean_coldest = self.df[self.df[temp_col] <= lower_decile_threshold][temp_col].mean()

            print(f"\nMean temperature (Hottest 10%): {mean_hottest:.2f} C")
            print(f"Mean temperature (Coldest 10%): {mean_coldest:.2f} C")

            if mean_coldest != 0:
                ratio = abs(mean_hottest / mean_coldest)
                print(f"Result: Hottest days are {ratio:.2f} times 'warmer' than coldest (by mean ratio).")
            else:
                print("Cannot calculate ratio (mean coldest is zero).")
