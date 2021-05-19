from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Претрага филмова')
window.geometry('350x200')
window.resizable(width=False, height=True)

background=PhotoImage(file='ha.png')
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def runSearch():
    print('Blah')

# Елемент за куцање речи
entry = Entry(
    window,
    width=28)
entry.grid(column=0, row=0, padx=5, pady=(5,0))

# Дугме за додавање кључних речи
addMovie = Button(window,
                text='Додај речи за претрагу',
                padx=18,
                pady=4,
                fg='white',
                bg='blue',
                command=runSearch)
addMovie.grid(column=0, row=1, padx=5, pady=(3, 8))

# Радио дугмићи
var = IntVar()
R1 = Radiobutton(window, text= 'По називу филма', variable=var, value=1,
                command=runSearch)
R1.configure(bg='blue', fg='white')
R1.grid(column=0, row=2)

R2 = Radiobutton(window, text= 'По жанру', variable=var, value=1,
                command=runSearch)
R2.configure(bg='blue', fg='white', width=14)
R2.grid(column=0, row=3)

# Дугме за претрагу
searchButton = Button(window, text='Претражи', padx=20,
                     fg='white', bg='blue', command=runSearch)
searchButton.grid(column=2, row=1, padx=25)

window.mainloop()