from posixpath import expanduser
from tkinter import *
from tkinter import ttk
from functools import partial
import importlib
import sys
import os

IOUtils = importlib.import_module('IOUtils')
Scraping = importlib.import_module('scraping')

window = Tk()
window.title('MovieSoup 1.0')
window.geometry('500x600')
# window.resizable(width=False, height=True)

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
entry.grid(column=0, row=0, padx=(5, 20), pady=(5,0), sticky='w')

def clearEntry():
    entry.delete(0,'end')

def addNew(event=None):
    if not entry.get() or addMovie.cget('state') == 'disabled':
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
addMovie.grid(column=0, row=1, padx=5, pady=(3, 8), sticky='w')

# Генерисање резултата
def generateResults(results):
    if results == '':
            return
    resultLabel = Label(window, text=results, bg='blue', fg='white').grid(column=2, row=5, sticky='w')

# Покретање претраге
def executeSearch():
    results = None
    searchOption = radioButtonVar.get()
    if searchOption == 1:
        results = Scraping.doSearchAll(IOUtils.returnOrCreateFile().split('\n'), searchOption)
    elif searchOption == 2:
        results = Scraping.doSearchAll(genresToSearch, searchOption)
    generateResults(results)


# Дугме за претрагу
searchButton = Button(window, text='Претражи', fg='white', bg='blue', command=executeSearch, width=15)
searchButton.grid(column=2, row=7, columnspan=2, sticky='w')

def interateOverCheckbuttonWidgets(state):
    for widget in window.winfo_children():
            if widget.winfo_class() == 'Checkbutton':
                widget.config(state=state)

def changeOptionStates(val):
    if val == 1:
        addMovie.config(state=ACTIVE)
    elif val == 2:
        interateOverCheckbuttonWidgets(ACTIVE)
    elif val == 3:
        pass

    if val != 1:
        addMovie.config(state=DISABLED)
    elif val != 2:
        interateOverCheckbuttonWidgets(DISABLED)
    elif val != 3:
        pass

genresToSearch = []

def addOrRemoveGenre(val):
    if val in genresToSearch:
        genresToSearch.remove(val)
        if(val == 'SF'):
            genresToSearch.remove('Fantastika')
    else:
        genresToSearch.append(val)
        if(val == 'SF'):
            genresToSearch.append('Fantastika')

# Genres
def genreButtons():
    action = Checkbutton(window, text='Акција', width=7, command=lambda: addOrRemoveGenre('Akcija'))
    action.grid(row=1, column=1, padx=(12,2), pady=(14,2))

    thriller = Checkbutton(window, text='Трилер   ', width=7, command=lambda: addOrRemoveGenre('Triler'))
    thriller.grid(row=1, column=2, padx=(2,2), pady=(14,2))

    romance = Checkbutton(window, text='Романтика ', width=9, command=lambda: addOrRemoveGenre('Romantika'))
    romance.grid(row=1, column=3, padx=(2,2), pady=(14,2), sticky='w')

    crime = Checkbutton(window, text='Крими', width=7, command=lambda: addOrRemoveGenre('KRIMINAL'))
    crime.grid(row=2, column=1, padx=(12,2), pady=(2,2))

    comedy = Checkbutton(window, text='Комедија', width=7, command=lambda: addOrRemoveGenre('Komedija'))
    comedy.grid(row=2, column=2, padx=(2,2), pady=(2,2))

    adventure = Checkbutton(window, text='Авантура    ', width=9, command=lambda: addOrRemoveGenre('Avantura'))
    adventure.grid(row=2, column=3, padx=(2,2), pady=(2,2), sticky='w')

    drama = Checkbutton(window, text='Драма', width=7, command=lambda: addOrRemoveGenre('Drama'))
    drama.grid(row=3, column=1, padx=(12,2), pady=(2,2))

    scifi = Checkbutton(window, text='Sci-Fi       ', width=7, command=lambda: addOrRemoveGenre('SF'))
    scifi.grid(row=3, column=2, padx=(2,2), pady=(2,2))

    family = Checkbutton(window, text='Породични', width=9, command=lambda: addOrRemoveGenre('Obitelj'))
    family.grid(row=3, column=3, padx=(2,2), pady=(2,2), sticky='w')

    horror = Checkbutton(window, text='Хорор     ', width=7, command=lambda: addOrRemoveGenre('Horror'))
    horror.grid(row=4, column=2, padx=(2,2), pady=(2,2))



genreButtons()

radioButtonVar = IntVar()
radioButtonVar.set('1')

# Radio buttons
byName = Radiobutton(window, variable=radioButtonVar ,value=1, text='По имену', command=lambda: changeOptionStates(1))
byName.grid(row=0, column=1, sticky='w', pady=(5,0), padx=(2,2))
byName.invoke()

byGenre = Radiobutton(window, variable=radioButtonVar ,value=2, text='По жанру', command=lambda: changeOptionStates(2))
byGenre.grid(row=0, column=2, sticky='w', pady=(5,0), padx=(2,2))

byYear = Radiobutton(window, variable=radioButtonVar ,value=3, text='По годинама', command=lambda: changeOptionStates(3))
byYear.grid(row=0, column=3, sticky='w', pady=(5,0), padx=(5,2))


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

if len(IOUtils.returnOrCreateFile().split('\n')) > 1:
    generateCurrentSearch()

window.mainloop()