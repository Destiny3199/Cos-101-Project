import tkinter as tk
from tkinter import messagebox

# Dictionary for English to Latin translations
Latin_dict = {
    "love": "amor",
    "friend": "amicus",
    "sun": "sol",
    "moon": "luna",
    "water": "aqua",
    "earth": "terra",
    "sky": "caelum",
    "star": "stella",
    "book": "liber",
    "time": "tempus",
    "light": "lux",
    "darkness": "tenebrae",
    "peace": "pax",
    "war": "bellum",
    "life": "vita",
    "death": "mors",
    "strength": "fortitudo",
    "knowledge": "scientia",
    "wisdom": "sapientia",
    "beauty": "pulchritudo"
}

Spanish_dict = {
    'hola': 'hello',
    'adiós': 'goodbye',
    'feliz': 'happy',
    'gracias': 'thank you',
    'por favor': 'please',
    'sí': 'yes',
    'claro': 'of course',
    'amor': 'love',
    'gato': 'cat',
    'perro': 'dog',
    'mañana': 'tomorrow',
    'buenas tardes': 'good afternoon',
    'buenas noches': 'good evening',
    'encantado': 'pleased to meet you',
    'hasta pronto': 'see you soon',
    'hasta luego': 'see you later',
    'hasta mañana': 'see you tomorrow',
    '¿cómo estás?': 'How are you?'
}


# Function to handle translation
def translate_word():
    word = entry.get().lower()
    if word in translation_dict:
        translated_word = translation_dict[word]
        result_label.config(text=f"translation: {translated_word}")
        result_label.config(text=f"translation: {translated_word}")
    else:
        messagebox.showerror("Error", "Word not found in the dictionary!")

# Function to handle dropdown selection
def dropdown_translate():
    word = dropdown_var.get().lower()
    if word in translation_dict:
        translated_word = translation_dict[word]
        result_label.config(text=f"translation: {translated_word}")
    else:
        messagebox.showerror("Error", "Word not found in the dictionary!")

# Function to clear the input field and reset
def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="Translation will appear here.")
    dropdown_var.set("")

# Create the main Tkinter window
root = tk.Tk()
root.title("Translator")
root.geometry("400x300")

# Create and place widgets
header_label = tk.Label(root, text="English to Translator", font=("Helvetica", 16))
header_label.pack(pady=10)

# Create Entry and Button for text input translation
text_label = tk.Label(root, text="Enter an English word:")
text_label.pack(pady=5)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_word)
translate_button.pack(pady=10)

# Create a dropdown menu for predefined words
dropdown_label = tk.Label(root, text="Or select from the list:")
dropdown_label.pack(pady=5)

dropdown_var = tk.StringVar(root)
dropdown_var.set("")  # Default to empty string
dropdown_menu = tk.OptionMenu(root, dropdown_var, *translation_dict.keys())
dropdown_menu.pack(pady=5)

dropdown_translate_button = tk.Button(root, text="Translate Selected", command=dropdown_translate)
dropdown_translate_button.pack(pady=10)

# Create clear input button
clear_button = tk.Button(root, text="Clear", command=clear_input)
clear_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="Translation will appear here.", font=("Helvetica", 12))
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
