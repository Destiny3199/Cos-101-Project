from tkinter import Tk,Entry,Button,Label,StringVar

windows = Tk()
windows.geometry("600x250")
windows.title("Portuguese Dictionary")

entry_text= Entry(windows)
entry_text.pack()

result = StringVar()
result_label = Label(windows, textvariable=result)
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

def translate_portuguese():
    word = entry_word.get().lower()
    if word in english_to_portuguese_dict:
        result.set(f"Translation (Portuguese): {english_to_portuguese_dict[word]}")
    else:
        result.set("Translation: Not found")

windows.mainloop()










