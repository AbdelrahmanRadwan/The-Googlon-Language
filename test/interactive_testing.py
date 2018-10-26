from language_model.googlon_language import GooglonLanguage

language_model = GooglonLanguage("")
while True:
    text = input(">> ")
    language_model.update_language_model(text=text)
    language_model.get_analytics()
