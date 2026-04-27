import re


class GenericAnalyzer:
    def count_sentences(self):
        endings = re.findall(r"[.!?]", self.text)

        self.declarative_sentences = endings.count(".")
        self.interrogative_sentences = endings.count("?")
        self.exclamative_sentences = endings.count("!")

        self.total_sentences = (
            self.declarative_sentences
            + self.interrogative_sentences
            + self.exclamative_sentences
        )

    def count_letters(self):
        letters = re.findall(r"\w", self.text)
        self.total_letters = len(letters)

    def count_words(self):
        words = re.findall(r"\w+", self.text)

        self.total_words = len(words)

    def count_smillies(self):
        smiles = re.findall(r"[:;]-*[\]\[()]+", self.text)

        self.total_smiles = len(smiles)

    def count_averages(self):
        self.average_words_per_sentence = self.total_words / self.total_sentences
        self.average_letters_per_word = self.total_letters / self.total_words
