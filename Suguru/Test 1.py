linie =  [(1, 1), (2, 0), (3, 1), (5, 1), (6, 0), (7, 1), (9, 1), (8, 2), (7, 3), (6, 4), (4, 4), (4, 2)]
okna =  [[(0, 0)], [(1, 0), (2, 0)], [(3, 0), (4, 0)], [(4, 1), (4, 2), (3, 2)], [(3, 1), (2, 1), (2, 2)], [(1, 2), (1, 1), (0, 1), (0, 2)]]
liczby =  [[1, 2, 1, 2, 1], ['.', '.', '.', '.', '.'], ['.', '.', '.', 2, 1]]

import Game

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

linie, okna, liczby = decrypt(crypt(linie, okna, liczby))

Game.Display(linie, okna, liczby)
