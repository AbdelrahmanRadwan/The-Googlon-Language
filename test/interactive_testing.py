import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from language_model.googlon_language import GooglonLanguage

language_model = GooglonLanguage("")
while True:
    text = input(">> ")
    language_model.update_language_model(text=text)
    language_model.print_analytics()
