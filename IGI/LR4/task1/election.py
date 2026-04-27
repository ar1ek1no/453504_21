import csv
import pickle
from task1.candidate import Candidate


class Election:
    TOTAL_ELECTORS = 2000
    PASS_THRESHOLD = 1/3

    def __init__(self):
        self.candidates = []

    def get_current_total_votes(self):
        return sum(c.votes for c in self.candidates)

    def add_candidate(self, surname, votes):
        if self.get_current_total_votes() + votes > self.TOTAL_ELECTORS:
            print(f"Error: total votes cannot exceed {self.TOTAL_ELECTORS}.")
            return False
        existing = self.find_candidate(surname)
        if existing:
            existing.votes += votes
        else:
            self.candidates.append(Candidate(surname, votes))
        return True

    def get_winners(self):
        threshold_value = self.TOTAL_ELECTORS * self.PASS_THRESHOLD
        passed = [c for c in self.candidates if c.votes >= threshold_value]
        return sorted(passed, key=lambda x: x.votes, reverse=True)

    def find_candidate(self, surname):
        return next((c for c in self.candidates if c.surname.lower() == surname.lower()), None)

    def save_csv(self):
        with open("elections.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Surname", "Votes"])
            for c in self.candidates:
                writer.writerow([c.surname, c.votes])

    def load_csv(self):
        try:
            self.candidates.clear()
            with open("elections.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.candidates.append(Candidate(row[0], int(row[1])))
        except FileNotFoundError:
            print("CSV file not found.")

    def save_pickle(self):
        with open("elections.pickle", "wb") as f:
            pickle.dump(self.candidates, f)

    def load_pickle(self):
        try:
            with open("elections.pickle", "rb") as f:
                self.candidates = pickle.load(f)
        except FileNotFoundError:
            print("Pickle file not found.")