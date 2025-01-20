from tkinter import Tk, Entry, Label, StringVar, Button

window = Tk()
window.geometry("600x250")
window.title("Spanish Dictionary")

label = Label(window, text="Spanish Translator", font=("Comic Sans MS",18))
label.pack(padx=20, pady=20)

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result, font=("Comic Sans MS", 14))
result_label.pack()

english_to_portuguese_dict = {
    "hello": "olá",
    "goodbye": "adeus",
    "happy": "feliz",
    "thank you": "obrigado",
    "please": "por favor",
    "yes": "sim",
    "of course": "claro",
    "love": "amor",
    "cat": "gato",
    "dog": "cachorro",
    "tomorrow": "amanhã",
    "good afternoon": "boa tarde",
    "good evening": "boa noite",
    "pleased to meet you": "prazer em conhecê-lo",
    "see you soon": "até logo",
    "see you later": "até mais tarde",
    "see you tomorrow": "até amanhã",
    "how are you?": "como você está?"
}

# English to Portuguese translation function
def translate_portuguese():
    word = entry_word.get().lower()
    if word in english_to_portuguese_dict:
        result.set(f"Translation (Portuguese): {english_to_portuguese_dict[word]}")
    else:
        result.set("Translation: Not found")
