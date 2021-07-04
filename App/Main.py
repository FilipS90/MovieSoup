from posixpath import expanduser
from tkinter import *
from tkinter import ttk
from functools import partial
import importlib
import sys
import os

IOUtils = importlib.import_module('IOUtil')
Scraping = importlib.import_module('ScrapingUtil')

window = Tk()
window.title('MovieSoup 1.0')
window.geometry('1020x350')
window.resizable(width=False, height=False)

nameInt = 0

def setConstantElementNames():
    global nameInt
    nameInt += 1
    return 'const' + str(nameInt)

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
background_label = Label(window, image=background, name=setConstantElementNames())
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Елемент за куцање речи
entry = Entry(
    window,
    width=28, 
    name=setConstantElementNames())
entry.grid(column=0, row=0, padx=(5, 20), pady=(5,0), sticky='w')

def clearEntry():
    entry.delete(0,'end')

def addNew(event=None):
    if not entry.get() or addMovie.cget('state') == 'disabled':
        return
    IOUtils.addNewLine(entry.get())
    clearEntry()
    refreshWindow('keywords')
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
                command=addNew,
                name=setConstantElementNames())
addMovie.grid(column=0, row=1, padx=5, pady=(3, 8), sticky='w')

# Генерисање резултата
def generateResults(results):
    if len(results) == 0:
        return
    resultsList = Listbox(window, bg='blue', fg='white', width=0, height=17, name='generated2')
    resultsList.grid(column=5, row=0, rowspan=12, padx=(15,0), pady=(5,0))
    for movie in results:
        resultsList.insert(END, movie)

# Покретање претраге
def executeSearch():
    results = None
    refreshWindow('generated')
    searchOption = radioButtonVar.get()
    if searchOption == 1:
        results = Scraping.doSearchAll(IOUtils.returnOrCreateFile().split('\n'), searchOption)
    elif searchOption == 2:
        results = Scraping.doSearchAll(genresToSearch, searchOption)
    elif searchOption == 3:
        print(fromYearInput.get() + ' ' + toYearInput.get())
        betweenYears = [fromYearInput.get(), toYearInput.get()]
        results = Scraping.doSearchAll(betweenYears, searchOption)
    generateResults(results)


# Дугме за претрагу
searchButton = Button(window, text='Претражи', fg='white', bg='green', command=executeSearch, width=10, name=setConstantElementNames())
searchButton.grid(column=1, row=11, columnspan=2, sticky='e')

# Genres
def generateGenreButtons():
    action = Checkbutton(window, text='Акција', width=7, command=lambda: addOrRemoveGenre('Akcija'), name=setConstantElementNames())
    action.grid(row=1, column=1, padx=(12,2), pady=(14,2))

    thriller = Checkbutton(window, text='Трилер   ', width=7, command=lambda: addOrRemoveGenre('Triler'), name=setConstantElementNames())
    thriller.grid(row=1, column=2, padx=(2,2), pady=(14,2))

    romance = Checkbutton(window, text='Романтика ', width=9, command=lambda: addOrRemoveGenre('Romantika'), name=setConstantElementNames())
    romance.grid(row=1, column=3, padx=(2,2), pady=(14,2), sticky='w')

    crime = Checkbutton(window, text='Крими', width=7, command=lambda: addOrRemoveGenre('KRIMINAL'), name=setConstantElementNames())
    crime.grid(row=2, column=1, padx=(12,2), pady=(2,2))

    comedy = Checkbutton(window, text='Комедија', width=7, command=lambda: addOrRemoveGenre('Komedija'), name=setConstantElementNames())
    comedy.grid(row=2, column=2, padx=(2,2), pady=(2,2))

    adventure = Checkbutton(window, text='Авантура    ', width=9, command=lambda: addOrRemoveGenre('Avantura'), name=setConstantElementNames())
    adventure.grid(row=2, column=3, padx=(2,2), pady=(2,2), sticky='w')

    drama = Checkbutton(window, text='Драма', width=7, command=lambda: addOrRemoveGenre('Drama'), name=setConstantElementNames())
    drama.grid(row=3, column=1, padx=(12,2), pady=(2,2))

    scifi = Checkbutton(window, text='Sci-Fi       ', width=7, command=lambda: addOrRemoveGenre('SF'), name=setConstantElementNames())
    scifi.grid(row=3, column=2, padx=(2,2), pady=(2,2))

    family = Checkbutton(window, text='Породични', width=9, command=lambda: addOrRemoveGenre('Obitelj'), name=setConstantElementNames())
    family.grid(row=3, column=3, padx=(2,2), pady=(2,2), sticky='w')

    horror = Checkbutton(window, text='Хорор     ', width=7, command=lambda: addOrRemoveGenre('Horror'), name=setConstantElementNames())
    horror.grid(row=4, column=2, padx=(2,2), pady=(2,2))

generateGenreButtons()

def interateOverCheckbuttonWidgets(newState):
    for widget in window.winfo_children():
            if widget.winfo_class() == 'Checkbutton':
                widget.config(state=newState)

def changeOptionStates(val):
    if val == 1:
        addMovie.config(state=ACTIVE)
    if val == 2:
        interateOverCheckbuttonWidgets(ACTIVE)
    if val == 3:
        interateOverCheckbuttonWidgets(DISABLED)

    if val != 1:
        addMovie.config(state=DISABLED)
    if val != 2:
        interateOverCheckbuttonWidgets(DISABLED)

genresToSearch = []

def addOrRemoveGenre(val):
    global genresToSearch
    if val in genresToSearch:
        genresToSearch.remove(val)
        if(val == 'SF'):
            genresToSearch.remove('Fantastika')
    else:
        genresToSearch.append(val)
        if(val == 'SF'):
            genresToSearch.append('Fantastika')

radioButtonVar = IntVar()
radioButtonVar.set('1')

# Radio buttons
byName = Radiobutton(window, variable=radioButtonVar ,value=1, text='По имену', command=lambda: changeOptionStates(1), name=setConstantElementNames())
byName.grid(row=0, column=1, sticky='w', pady=(5,0), padx=(2,2))
byName.invoke()

byGenre = Radiobutton(window, variable=radioButtonVar ,value=2, text='По жанру', command=lambda: changeOptionStates(2), name=setConstantElementNames())
byGenre.grid(row=0, column=2, sticky='w', pady=(5,0), padx=(2,2))

byYear = Radiobutton(window, variable=radioButtonVar ,value=3, text='По годинама', command=lambda: changeOptionStates(3), name=setConstantElementNames())
byYear.grid(row=0, column=3, sticky='w', pady=(5,0), padx=(5,2))

fromYear = Label(window, text='Од године', bg='blue', fg='white', width=8, name=setConstantElementNames())
fromYear.grid(row=7, column=1)

fromYearInput = Entry(window, width=10, name=setConstantElementNames())
fromYearInput.grid(row=8, column=1)

toYear = Label(window, text='До године', bg='blue', fg='white', width=8, name=setConstantElementNames())
toYear.grid(row=7, column=3)

toYearInput = Entry(window, width=10, name=setConstantElementNames())
toYearInput.grid(row=8, column=3)

# Освежи прозор
def refreshWindow(widgetToDelete):
    for widget in window.winfo_children():
        if str(widget).split(".")[-1].startswith(widgetToDelete):
            widget.destroy()

resultsList = None

# Уклони кључну реч / назив филма
def removeKeyword(event):
    global resultsList
    for i in resultsList.curselection():
        val = resultsList.get(i)
    IOUtils.deleteLine(val)
    refreshWindow('keywords')
    generateCurrentSearch()

# Генерисање тренутних кључних речи / имена филмова
def generateCurrentSearch():
    movies = IOUtils.returnOrCreateFile().split('\n')
    global resultsList
    resultsList = Listbox(window, bg='blue', fg='white', width=28, height=13, name='keywords')
    resultsList.grid(column=0, row=2, padx=(5,0), pady=2, rowspan=10, sticky='w')
    resultsList.bind('<Double-1>', removeKeyword)

    for movie in movies:
        resultsList.insert(END, movie)

if len(IOUtils.returnOrCreateFile().split('\n')) > 1:
    generateCurrentSearch()

window.mainloop()