import tkinter as tk
from tkinter import *
import Game
import Add
import sqlite3

addedbase = sqlite3.connect('suguru.db')
do_addedbase = addedbase.cursor()
levelsbase = sqlite3.connect('levels.db')
do_levelsbase = levelsbase.cursor()

do_addedbase.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
name TEXT NOT NULL);''')
do_levelsbase.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
name TEXT NOT NULL);''')

def crypt(liniee, oknaa,  liczbyy):
    output = "L "
    for x in liniee:
        for c in x:
            output += str(c) + " "

    output += "O "

    for _ in oknaa:
        for x in _:
            for c in x:
                output += str(c) + " "
        output += "e "

    output += "K "

    for x in liczbyy:
        for c in x:
            output += str(c) + " "
        output += "e "

    return output

def decrypt(string):
    typeee = ""
    c = 0
    lista = []
    okno = []
    linieout = []
    oknaout = []
    liczbyout = []
    for x in string:
        if x == "L":
            typeee = "L"
            continue
        if x == "O":
            typeee = "O"
            continue
        if x == "K":
            typeee = "K"
            continue
        if x == " ":
            continue
        if typeee == "L":
            lista.append(int(x))
            c += 1
            if c == 2:
                linieout.append(lista)
                lista = []
                c = 0
        if typeee == "O":
            if x == "e":
                oknaout.append(okno)
                okno = []
                continue
            lista.append(int(x))
            c += 1
            if c == 2:
                okno.append(lista)
                lista = []
                c = 0
        if typeee == "K":
            if x == "e":
                liczbyout.append(lista)
                lista = []
                continue
            lista.append(int(x) if x != "." else x)
    return linieout, oknaout, liczbyout

do_addedbase.execute('SELECT * FROM sheets')
sheets = do_addedbase.fetchall()
do_levelsbase.execute('SELECT * FROM sheets')
levelslist = do_levelsbase.fetchall()

class App:
    def __init__(self):
        self.program = tk.Tk(className="Suguru")
        bg = tk.PhotoImage(file="background.png")
        self.bg = tk.Label(self.program, image=bg)
        self.bg.pack()
        self.levelsbutton = Button(self.program, text="Levels", command=lambda: self.levels())
        self.levelsbutton.pack()
        self.addlevelsbutton = Button(self.program, text="Add New Suguru", command=lambda: self.Addlvl())
        self.addlevelsbutton.pack()
        self.addedlevels = Button(self.program, text="Added Suguru", command=lambda: self.added())
        self.addedlevels.pack()
        self.program.mainloop()

    def Click(self, lista):
        linie, okna, liczby = lista[0], lista[1], lista[2]
        Game.Display(linie, okna, liczby)

    def Addlvl(self):
        Add.Display()

    def added(self):
        def Click(lista):
            linie, okna, liczby = decrypt(lista)
            Game.Display(linie, okna, liczby)

        def Delete(id, n):
            do_addedbase.execute('DELETE FROM sheets WHERE id = ?', (id,))
            addedbase.commit()
            for n, i in enumerate(sheets):
                levels[n].pack_forget()
                deletes[n].pack_forget()
            exitbtn.pack_forget()
            self.added()
        def exit(levels, exitbtn):
            for n, i in enumerate(sheets):
                levels[n].pack_forget()
                deletes[n].pack_forget()
            self.bg.pack()
            self.levelsbutton.pack()
            self.addlevelsbutton.pack()
            self.addedlevels.pack()
            exitbtn.pack_forget()
        self.bg.pack_forget()
        self.levelsbutton.pack_forget()
        self.addedlevels.pack_forget()
        self.addlevelsbutton.pack_forget()
        levels = []
        deletes = []
        do_addedbase.execute('SELECT * FROM sheets')
        addedbase.commit()
        sheets = do_addedbase.fetchall()
        for n, i in enumerate(sheets):
            levels.append(Button(self.program, text = "My Suguru " + str(n + 1), command = lambda x = decrypt(i[1]): self.Click(x)))
            levels[n].pack()
            deletes.append(Button(self.program, text = "Delete", command = lambda x = i[0] : Delete(x, n)))
            deletes[n].pack()
        exitbtn = Button(self.program, text = "Back", command = lambda : exit(levels, exitbtn))
        exitbtn.pack()

    def levels(self):
        def exit(levels, exitbtn):
            for n, i in enumerate(sheets):
                levels[n].pack_forget()
            self.bg.pack()
            self.levelsbutton.pack()
            self.addlevelsbutton.pack()
            self.addedlevels.pack()
            exitbtn.pack_forget()
        self.bg.pack_forget()
        self.levelsbutton.pack_forget()
        self.addedlevels.pack_forget()
        self.addlevelsbutton.pack_forget()
        levels = []
        do_levelsbase.execute('SELECT * FROM sheets')
        levelsbase.commit()
        sheets = do_levelsbase.fetchall()
        for n, i in enumerate(sheets):
            levels.append(Button(self.program, text="Level " + str(n + 1), command=lambda x = decrypt(i[1]): self.Click(x)))
            levels[n].pack()
        exitbtn = Button(self.program, text = "Back", command = lambda : exit(levels, exitbtn))
        exitbtn.pack()

App()

addedbase.commit()
addedbase.close()
levelsbase.commit()
levelsbase.close()
