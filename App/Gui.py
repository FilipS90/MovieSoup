from tkinter import *
from tkinter import ttk
import importlib

IOUtils = importlib.import_module('IOUtils')
Scraping = importlib.import_module('scraping')

window = Tk()
window.title('MovieSoup 1.0')
window.geometry('350x200')
window.resizable(width=False, height=True)

background=PhotoImage(file='ha.png')
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Елемент за куцање речи
entry = Entry(
    window,
    width=28)
entry.grid(column=0, row=0, padx=5, pady=(5,0))

def addNew():
    IOUtils.addNewLine(entry.get())

# Дугме за додавање кључних речи
addMovie = Button(window,
                text='Додај речи за претрагу',
                padx=18,
                pady=4,
                fg='white',
                bg='blue',
                command=addNew)
addMovie.grid(column=0, row=1, padx=5, pady=(3, 8))

# Дугме за претрагу
searchButton = Button(window, text='Претражи', padx=20,
                     fg='white', bg='blue', command=Scraping.doSearch)
searchButton.grid(column=2, row=1, padx=25)

currentMovieSearch = IOUtils.returnOrCreateFile().split('\n')

def generateCurrentSearch():
    for idx, val in enumerate(currentMovieSearch):
        label = Label(window, text=val)
        label.grid(column=0, row=idx+2)

generateCurrentSearch()

window.mainloop()


# # Опције
# OPTIONS = [
#     'По називу филма',
#     'По жанру'
# ]

# var = StringVar(window)
# var.set(OPTIONS[0])
# dropDown = OptionMenu(window, var, *OPTIONS)
# dropDown.configure(bg='blue', fg='white')
# dropDown.grid(column=0, row=2, padx=5, pady=(3, 8))

# Жанрови
# c1 = Checkbutton(window, text='Акција',variable=1, onvalue=1, offvalue=0, command=print('ah'))
# c1.grid(column=0, row=3, padx=5, pady=(3, 8))

# c2 = Checkbutton(window, text='Драма',variable=1, onvalue=1, offvalue=0, command=print('ah'))
# c2.grid(column=0, row=4, padx=5, pady=(3, 8))