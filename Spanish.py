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

Dictionary = {
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
