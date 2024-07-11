import tkinter as tk
from tkinter import *
import main as Main
import sqlite3

addedbase = sqlite3.connect('sudoku.db')
do_addedbase = addedbase.cursor()
levelsbase = sqlite3.connect('levels.db')
do_levelsbase = levelsbase.cursor()

do_addedbase.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
name TEXT NOT NULL);''')
do_levelsbase.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
name TEXT NOT NULL);''')

def crypt(lista):
    out = ""
    for x in range(9):
        t = [str(_) for _ in lista[x]]
        out += " ".join(t) + " "
    return out

def decrypt(string):
    i = 0
    lista = [[]]
    for x in string:
        if x == " ":
            continue
        if i == 9:
            i = 0
            lista.append([])
        lista[-1].append(x if x == "." else int(x))
        i += 1
    return lista

do_addedbase.execute('SELECT * FROM sheets')
sheets = do_addedbase.fetchall()
do_levelsbase.execute('SELECT * FROM sheets')
levelslist = do_levelsbase.fetchall()

class App:
    def __init__(self):
        self.program = tk.Tk(className="Sudoku")
        bg = tk.PhotoImage(file="background.png")
        self.bg = tk.Label(self.program, image=bg)
        self.bg.pack()
        self.levelsbutton = Button(self.program, text="Levels", command=lambda: self.levels())
        self.levelsbutton.pack()
        self.addlevelsbutton = Button(self.program, text="Add New Sudoku", command=lambda: self.Addlvl())
        self.addlevelsbutton.pack()
        self.addedlevels = Button(self.program, text="Added Sudoku", command=lambda: self.added())
        self.addedlevels.pack()
        self.program.mainloop()

    def Click(self, lista):
        Main.Game(lista)

    def Addlvl(self):
        Main.Add()

    def added(self):
        def Click(lista):
            print(lista)
            Main.Game(lista)

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
            levels.append(Button(self.program, text = "My Sudoku " + str(n + 1), command = lambda x = decrypt(i[1]): self.Click(x)))
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
