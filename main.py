from tkinter import Tk,Entry,Button,Label,StringVar

windows = Tk()
windows.geometry("600x250")
windows.title("Portuguese Dictionary")

entry_text= Entry(windows)
entry_text.pack()

result = StringVar()
result_label = Label(windows, textvariable=result)
result_label.pack()


portuguese_dict = {"ola":"hello",
                   "amor":"love",
                   "amigo":"friends",
                   "casa":"house",
                   "escola":"school",
                   "trabalho":"work",
                   "comida":'food',
                   "agua":"water",
                   "sol":"sun",
                   "lua":"moon",
                   "livro":'book',
                   "musica":'music',
                   "coracao":"heart",
                   "familia":'family',
                   "viagem":"travel",
                   "tempo":"time",
                   "dinheiro":"money",
                   "suade":"health",
                   "falicidade":"happiness",
                   "esperanca":"hope"
}

def search(word):
    if word in portuguese_dict:
        result.set(portuguese_dict[word])
        print(portuguese_dict[word])
    else:
        result.set("not found")
        print("not found")
search_btn = Button(windows,text="search",command=lambda: search(entry_text.get()))
search_btn.pack()

windows.mainloop()










