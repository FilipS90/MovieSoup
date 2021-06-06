from tkinter import *
from functools import partial
import importlib
import sys
import os

IOUtils = importlib.import_module('IOUtils')
Scraping = importlib.import_module('scraping')

window = Tk()
window.title('MovieSoup 1.0')
window.geometry('500x600')
window.resizable(width=False, height=True)

# Да би Pyinstaller повукао и слику у извршни фајл
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

img = resource_path("backgroundImg.png")

background=PhotoImage(file=img)
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Елемент за куцање речи
entry = Entry(
    window,
    width=28)
entry.grid(column=0, row=0, padx=5, pady=(5,0))

def clearEntry():
    entry.delete(0,'end')

def addNew(event=None):
    if not entry.get():
        return
    IOUtils.addNewLine(entry.get())
    clearEntry()
    generateCurrentSearch()

# Повезивање addNew методе са ентер дугметом
window.bind('<Return>', addNew)

# Дугме за додавање кључних речи
addMovie = Button(window,
                text='Додај речи за претрагу',
                padx=18,
                pady=4,
                fg='white',
                bg='blue',
                command=addNew)
addMovie.grid(column=0, row=1, padx=5, pady=(3, 8))

# Генерисање резултата
def generateResults():
    results = Scraping.doSearch_All(IOUtils.returnOrCreateFile().split('\n'))
    if results == '':
        return
    resultLabel = Label(window, text=results, bg='blue', fg='white').grid(column=2, row=2, sticky='w')

# Дугме за претрагу
searchButton = Button(window, text='Претражи', padx=20,
                     fg='white', bg='blue', command=generateResults)
searchButton.grid(column=2, row=1, padx=25)

# Уклони кључну реч / назив филма
def removeKeyword(val):
    for widget in window.winfo_children():
        if widget == searchButton or widget == addMovie or widget == entry or widget == background_label:
            continue
        else: 
            widget.destroy()

    IOUtils.deleteLine(val)
    generateCurrentSearch()

# Генерисање тренутних кључних речи / имена филмова
def generateCurrentSearch():
    for idx, val in enumerate(IOUtils.returnOrCreateFile().split('\n')):
        if val == '':
            continue
        button = Button(window, text=val, bg='blue', fg='white', command=partial(removeKeyword, val))
        button.grid(column=0, row=idx+2, sticky='w', padx=(5,0), pady=2, columnspan=2)
        window.lastRow = idx+2

if len(IOUtils.returnOrCreateFile().split('\n')) > 1:
    generateCurrentSearch()

window.mainloop()