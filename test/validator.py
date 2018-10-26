import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from helper_functions.utils import (read_json_content, write_json_content)

from language_model.googlon_language import GooglonLanguage


language_model = GooglonLanguage("")
test_cases = read_json_content()
test_cases_results = list()

for test_case in test_cases:
    language_model.update_language_model(test_case["text"])
    test_cases_results.append(language_model.get_analytics())

write_json_content(test_cases_results)
