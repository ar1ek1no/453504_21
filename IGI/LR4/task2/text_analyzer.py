from .generic_analyzer import GenericAnalyzer
from .variant_analyzer import VariantAnalyzer


class TextAnalyzer(GenericAnalyzer, VariantAnalyzer):
    def __init__(self, text):
        self.text = text

        self.count_sentences()
        self.count_letters()
        self.count_words()
        self.count_smillies()
        self.count_averages()

        self.find_commapairs()
        self.find_phones()
        self.find_glasogl()
        self.count_spacerounded()

    @staticmethod
    def from_file(filename):
        with open(filename, "r") as f:
            return TextAnalyzer(f.read())

    def __str__(self):
        report = f"Sentences: {self.total_sentences}\n"
        report += f"Declarative sentences: {self.declarative_sentences}\n"
        report += f"Interrogative sentences: {self.interrogative_sentences}\n"
        report += f"Exclamative sentences: {self.exclamative_sentences}\n"
        report += f"Words: {self.total_words}\n"
        report += f"Letters: {self.total_letters}\n"
        report += f"Average words per sentence: {self.average_words_per_sentence}\n"
        report += f"Average letters per word: {self.average_letters_per_word}\n"
        report += f"Smileys: {self.total_smiles}\n"
        report += f"Phones: {self.phones}\n"
        report += f"Comma pairs: {self.commapairs}\n"
        report += f"Glascogl: {self.glasogl}\n"
        report += f"Spacerounded: {self.spacerounded}\n"

        return report