from helper_functions.utils import *


class GooglonLanguage:
    def __init__(self, text: str):
        self.text = text
        self.text_tokens = self.text.split()
        self.number_of_prepositions = 0
        self.number_of_verbs = 0
        self.number_of_subjunctive_form_verbs = 0
        self.number_of_distinct_pretty_numbers = 0
        self.ordered_vocabulary = []
        self.pretty_numbers = []

    def annotate_tokens(self):
        for token in self.text_tokens:
            if is_preposition(token):
                self.number_of_prepositions += 1

            if is_verb(token):
                self.number_of_verbs += 1

            if is_verb_in_subjunctive_form(token):
                self.number_of_subjunctive_form_verbs += 1

            if is_pretty_number(token):
                self.pretty_numbers.append(word_to_number(token))

            self.number_of_distinct_pretty_numbers = len(set(self.pretty_numbers))
            self.ordered_vocabulary = googlon_sort(words=list(set(self.text_tokens)))

    def get_number_of_prepositions(self):
        return self.number_of_prepositions

    def get_number_of_verbs(self):
        return self.number_of_verbs

    def get_number_of_subjunctive_form_verbs(self):
        return self.number_of_subjunctive_form_verbs

    def get_ordered_distinct_words(self):
        return self.ordered_vocabulary

    def get_number_of_distinct_pretty_numbers(self):
        return self.number_of_distinct_pretty_numbers

    def update_language_model(self, text):
        self.text = text
        self.text_tokens = self.text.split()
        self.number_of_prepositions = 0
        self.number_of_verbs = 0
        self.number_of_subjunctive_form_verbs = 0
        self.number_of_distinct_pretty_numbers = 0
        self.ordered_vocabulary = []
        self.pretty_numbers = []
        self.annotate_tokens()

    def print_analytics(self):
        print("1) There are {} prepositions in the text".format(self.get_number_of_prepositions()))
        print("2) There are {} verbs in the text".format(self.get_number_of_verbs()))
        print("3) There are {} subjunctive verbs in the text".format(self.get_number_of_subjunctive_form_verbs()))
        print("4) Vocabulary list:{}".format(self.get_ordered_distinct_words()))
        print("5) There are {} distinct pretty numbers in the text".format(self.get_number_of_distinct_pretty_numbers()))

    def get_analytics(self):
        analytics = dict()
        analytics["prepositions"] = self.get_number_of_prepositions()
        analytics["verbs"] = self.get_number_of_verbs()
        analytics["subjunctive verbs"] = self.get_number_of_subjunctive_form_verbs()
        analytics["Vocabulary list"] = self.get_ordered_distinct_words()
        analytics["distinct pretty numbers"] = self.get_number_of_distinct_pretty_numbers()
        return analytics
