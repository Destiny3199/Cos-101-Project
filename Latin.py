import tkinter as tk
from tkinter import messagebox

# Dictionary for English to Latin translations
english_to_latin_dict = {
    "hello": "salve",
    "goodbye": "vale",
    "happy": "felix",
    "thank you": "gratias",
    "please": "quaeso",
    "yes": "ita vero",
    "of course": "certo",
    "love": "amor",
    "cat": "felis",
    "dog": "canis",
    "tomorrow": "cras",
    "good afternoon": "bona vespera",
    "good evening": "bona nox",
    "pleased to meet you": "placet te convenire",
    "see you soon": "mox videbimus",
    "see you later": "videbimus postea",
    "see you tomorrow": "videbimus cras",
    "how are you?": "quomodo agitur?"
}

# English to Latin translation function
def translate_latin():
    word = entry_word.get().lower()
    if word in english_to_latin_dict:
        result.set(f"Translation (Latin): {english_to_latin_dict[word]}")
    else:
        result.set("Translation: Not found")

# Run the Tkinter event loop
root.mainloop()
