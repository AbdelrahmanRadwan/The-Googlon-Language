from helper_functions.constants import (googlon_to_english_dict, googlon_to_numbers_dict)


def is_foo_letter(character):
    return character in ['u', 'd', 'x', 's', 'm', 'p', 'f']


def is_bar_letter(character):
    return not is_foo_letter(character)


def is_preposition(word: str):
    """
    If the word has a foo letter at the end, doesn't have u inside, and is a 6-letter word, it's a preposition.
    If any of these three rules was broken, then it's not!
    :param word: A string of an English letters plain text.
    :return: is a preposition or not!
    """
    if len(word) != 6 or 'u' in word or is_bar_letter(word[-1]):
        return False
    return True


def is_verb(word: str):
    """
    If the word ends with a bar letter, and has more than 5 letters, then it's a verb
    :param word: A string of an English letters plain text.
    :return: is a verb or not!
    """
    if len(word) < 6 or is_foo_letter(word[-1]):
        return False
    return True


def is_verb_in_subjunctive_form(word: str):
    return is_verb(word) and is_bar_letter(word[0])


def googlon_sort(words: list()):
    """
    Sort list of words in lexicographical order based on this characters emplacement:
    (self, s, x, o, c, q, n, m, w, p, f, y, h, e, l, j, r, d, g, u, i)
    :param words: list of strings
    :return: the words sorted lexicographically
    """

    def sorting_custom_key(word):
        return "".join([googlon_to_english_dict[char] for char in word])

    return sorted(words, key=sorting_custom_key)


def word_to_number(word: str):
    number = 0
    base = 1
    for character in word:
        number += googlon_to_numbers_dict[character] * base
        base *= 20

    return number


def is_pretty_number(word: str):
    number = word_to_number(word=word)
    return number >= 81827 and number % 3 == 0
