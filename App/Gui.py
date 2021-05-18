from tkinter import *
from tkinter import ttk

backgroundColor = 'orange'

window = Tk()
window.title('Претрага филмова')
window.geometry('350x200')
window.resizable(width=False, height=True)
window.configure(background=backgroundColor)

def runSearch():
    print('Blah')

# Елемент за куцање речи
entry = Entry(
    window,
    width=28)
entry.grid(column=0, row=0, padx=5)

# Дугме за додавање кључних речи
addMovie = Button(window,
                text='Додај речи за претрагу',
                padx=18,
                pady=4,
                fg='white',
                bg='blue',
                command=runSearch)
addMovie.grid(column=0, row=1, padx=5, pady=(3, 5))

# Дугме за претрагу
searchButton = Button(window, text='Претражи', padx=20,
                     fg='white', bg='blue', command=runSearch)
searchButton.grid(column=2, row=1, padx=25)

window.mainloop()