import tkinter as tk
from tkinter import ttk

english_to_spanish_dict = {
    'hello': 'hola', 
    'goodbye': 'adiós', 
    'happy': 'feliz',
    'thank you': 'gracias'
    'please': 'por favor',
    'yes': 'sí', 
    'of course': 'claro', 
    'love': 'amor',
    'cat': 'gato',
    'dog': 'perro',
    'tomorrow': 'mañana', 
    'good afternoon': 'buenas tardes',
    'good evening': 'buenas noches',
    'pleased to meet you': 'encantado',
    'see you soon': 'hasta pronto',
    'see you later': 'hasta luego',
    'see you tomorrow': 'hasta mañana',
    'how are you?': '¿cómo estás?'
}

english_to_latin_dict = {
    'hello': 'salve', 'goodbye': 'vale', 'happy': 'felix', 'thank you': 'gratias', 'please': 'quaeso',
    'yes': 'ita vero', 'of course': 'certo', 'love': 'amor', 'cat': 'felis', 'dog': 'canis',
    'tomorrow': 'cras', 'good afternoon': 'bona vespera', 'good evening': 'bona nox',
    'pleased to meet you': 'placet te convenire',
    'see you soon': 'mox videbimus', 'see you later': 'videbimus postea', 'see you tomorrow': 'videbimus cras',
    'how are you?': 'quomodo agitur?'
}

english_to_german_dict = {
    'hello': 'hallo',
    'goodbye': 'auf wiedersehen',
    'happy': 'glücklich',
    'thank you': 'danke',
    'please': 'bitte',
    'yes': 'ja',
    'of course': 'natürlich',
    'love': 'liebe',
    'cat': 'katze',
    'dog': 'hund',
    'tomorrow': 'morgen',
    'good afternoon': 'guten nachmittag',
    'good evening': 'guten abend',
    'pleased to meet you': 'freut mich dich kennenzulernen',
    'see you soon': 'bis bald',
    'see you later': 'bis später',
    'see you tomorrow': 'bis morgen',
    'how are you?': 'wie gehts?',
}

english_to_korean_dict = {
    'hello': '안녕하세요 (annyeonghaseyo)', 'goodbye': '안녕히 가세요 (annyeonghi gaseyo)', 'happy': '행복해요 (haengbokhaeyo)',
    'thank you': '감사합니다 (kamsahamnida)', 'please': '제발 (jebal)', 'yes': '네 (dae)', 'of course': '물론이죠 (mullonijyo)',
    'love': '사랑해요 (salanghaeyo)', 'cat': '고양이 (goyangi)', 'dog': '개 (gae)', 'tomorrow': '내일 (naeil)',
    'good afternoon': '좋은 오후 (joeun ohu)', 'good evening': '좋은 저녁 (joeun jeonyeok)',
    'pleased to meet you': '만나서 반가워요 (mannaseo bangawoyo)',
    'see you soon': '곧 봐요 (god bwayo)', 'see you later': '나중에 봐요 (najunge bwayo)',
    'see you tomorrow': '내일 봐요 (naeil bwayo)',
    'how are you?': '어떻게 지내세요? (eotteoke jinaeseyo?)'
}

english_to_portuguese_dict = {
    'hello': 'olá', 'goodbye': 'adeus', 'happy': 'feliz', 'thank you': 'obrigado', 'please': 'por favor', 'yes': 'sim',
    'of course': 'claro', 'love': 'amor', 'cat': 'gato', 'dog': 'cachorro', 'tomorrow': 'amanhã',
    'good afternoon': 'boa tarde',
    'good evening': 'boa noite', 'pleased to meet you': 'prazer em conhecê-lo', 'see you soon': 'até logo',
    'see you later': 'até mais tarde',
    'see you tomorrow': 'até amanhã', 'how are you?': 'como você está?'
}

def translate():
    word = entry_word.get().lower()
    selected_language = language_var.get()

    translation = "Translation: Not found"

    # Get the appropriate dictionary based on language selection
    if selected_language == 'Spanish':
        translation = english_to_spanish_dict.get(word, translation)
    elif selected_language == 'Latin':
        translation = english_to_latin_dict.get(word, translation)
    elif selected_language == 'German':
        translation = english_to_german_dict.get(word, translation)
    elif selected_language == 'Korean':
        translation = english_to_korean_dict.get(word, translation)
    elif selected_language == 'Portuguese':
        translation = english_to_portuguese_dict.get(word, translation)

    result.set(translation)


def clear_input():
    entry_word.delete(0, tk.END)
    result.set("")


def update_status():
    selected_language = language_var.get()
    status_label.config(text=f"Selected language: {selected_language}")


window = tk.Tk()
window.geometry("600x500")
window.title("Multi-Translator")

header_label = tk.Label(window, text="Multi-Translator", font=("Comic Sans MS", 18))
header_label.pack(padx=20, pady=20)

entry_word = tk.Entry(window, font=("Comic Sans MS", 14), width=30)
entry_word.pack(pady=10)

language_var = tk.StringVar()
language_combobox = ttk.Combobox(window, textvariable=language_var,
                                 values=["Spanish", "Latin", "German", "Korean", "Portuguese"],
                                 font=("Comic Sans MS", 14))
language_combobox.set("Select Language")  # Default text
language_combobox.pack(pady=10)

translate_button = tk.Button(window, text="Translate", font=("Times New Roman", 14), command=translate)
translate_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear", font=("Times New Roman", 14), command=clear_input)
clear_button.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Comic Sans MS", 14))
result_label.pack(pady=20)

status_label = tk.Label(window, text="Selected language: None", font=("Comic Sans MS", 12), fg="gray")
status_label.pack(side="bottom", fill="x")

language_combobox.bind("<<ComboboxSelected>>", lambda event: update_status())

window.mainloop()
