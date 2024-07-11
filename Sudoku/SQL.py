import sqlite3

base = sqlite3.connect('sudoku.db')
do = base.cursor()

kartka = [[".", 7, ".", ".", 5, ".", ".", 9, 2],
          [2, 5, 9, 1, ".", ".", 6, 3, 4],
          [".", ".", ".", 4, ".", 2, 5, ".", "."],
          [3, ".", 2, 7, 1, 6, ".", ".", "."],
          [5, ".", 1, 2, ".", ".", ".", ".", "."],
          [".", ".", ".", 5, ".", ".", ".", 2, 3],
          [6, 2, ".", ".", ".", ".", ".", ".", 5],
          [".", ".", 7, ".", ".", ".", ".", ".", 6],
          [".", 8, 5, ".", ".", 4, ".", 1, "."]]

do.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
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

#do.execute('''INSERT INTO sheets (name) VALUES (?);''', (crypt(kartka), ))
#do.execute('DELETE FROM sheets WHERE id = ?', (1,))

do.execute('SELECT * FROM sheets')

rows = do.fetchall()

for x in rows:
    print(decrypt(x[1]))

base.commit()
base.close()
