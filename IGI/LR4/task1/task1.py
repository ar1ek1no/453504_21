from common.action import Action
from common.task import Task
from common.ui import read_int, read_str

from .candidate import Candidate
from .election import Election


class Task1(Task):
    name = "Task 1 (Elections)"

    def __init__(self):
        self.election = Election()

    def actions(self):
        return super().actions() + [
            Action("Add Candidate", self.add_cand),
            Action("Show Results", self.show_results),
            Action("Search Candidate", self.search_cand),
            Action("Save (CSV)", self.election.save_csv),
            Action("Load (CSV)", self.election.load_csv),
            Action("Save (Pickle)", self.election.save_pickle),
            Action("Load (Pickle)", self.election.load_pickle),
        ]

    def add_cand(self):
        surname = read_str("Enter surname: ")
        votes = read_int("Enter votes: ", min=0, max=2000)
        self.election.add_candidate(surname, votes)

    def show_results(self):
        winners = self.election.get_winners()
        total_cast = self.election.get_current_total_votes()

        print(f"\n--- Election Status ---")
        print(f"Total votes cast: {total_cast} / {self.election.TOTAL_ELECTORS}")

        if not winners:
            print("RESULT: Repeat elections required (no candidate reached 1/3 of votes).")
        else:
            print(f"Winners ({len(winners)}):")
            for c in winners:
                print(f"- {c.surname}: {c.votes} votes")

    def search_cand(self):
        surname = read_str("Enter surname to find: ")
        c = self.election.find_candidate(surname)
        if c:
            print(f"Found: {c.surname} with {c.votes} votes.")
        else:
            print("Candidate not found.")