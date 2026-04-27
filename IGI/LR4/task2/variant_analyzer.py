import re


class VariantAnalyzer:
    def find_phones(self):
        self.phones = re.findall(r"29\d{7}", self.text)

    def find_glasogl(self):
        self.glasogl = [
            x.strip()
            for x in re.findall(
                r"($|\s)[a-zA-Z][BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz][AaOoUuEeIiYy]\w+",
                self.text,
            )
        ]

    def count_spacerounded(self):
        self.spacerounded = len(re.findall(r" \w+ ", self.text))

    def count_letters(self):
        letters = re.findall(r"\w", self.text)
        self.letter_counts = {}
        for l in letters:
            self.letter_counts[l] = self.letter_counts.get(l, 0) + 1

    def find_commapairs(self):
        self.commapairs = re.findall(r"\w+,\s?\w+", self.text)
        self.commapairs.sort()
