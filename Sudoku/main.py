import random, copy

kartka = []

def Bugs(lista):
    for n, x in enumerate(lista):
        for i in range(1, 10):
            if x.count(i) > 1:
                return "Error too much in line: " + str(n + 1) + " " +"".join(str(_) for _ in x)

    for x in range(1, 10):
        n = x
        c = Okna(x, lista)
        x = []
        for _ in c:
            x += _
        for i in range(1, 10):
            if x.count(i) > 1:
                return "Error too much in window: " + str(n) + " " + "".join(str(_) for _ in x)

    for x in range(9):
        c = []
        for i in range(9):
            c += [lista[i][x]]
        for i in range(9):
            if c.count(i) > 1:
                return "Error too much in line: " + str(x + 1) + " " + "".join(str(_) for _ in c)

    for x in range(len(lista)):
        if len(kartka[x]) != 9:
            return "Error line: " + str(x + 1)

    return True

def Okna(n, lista):
    if n < 4:
        r = 3 * n
        i = 3
    elif n < 7:
        r = (n - 3) * 3
        i = 6
    else:
        r = (n - 6) * 3
        i = 9
    ret = []
    for x in range(i - 3, i):
        ret.append(lista[x][r - 3:r])
    return ret

def UpOkna(n, ciag):
    if n < 4:
        r = 3 * n
        i = 3
    elif n < 7:
        r = (n - 3) * 3
        i = 6
    else:
        r = (n - 6) * 3
        i = 9
    for j, x in enumerate(range(i - 3, i)):
        kartka[x][r - 3:r] = ciag[j]

def Pion(n):
    n -= 1
    c = []
    for x in range(9):
        c += [kartka[x][n]]
    return c

def UpPion(n, ciag):
    n -= 1
    for x in range(9):
        kartka[x][n] = ciag[x]

def End(ciag):
    for x in range(9):
        for xx in range(9):
            if ciag[x][xx] == "." or type(ciag[x][xx]) == list:
                return None

    if Bugs(ciag) is True:
        return True
    return False

def Wypisz():
    print()
    c = 0
    for _ in range(3):
        for x in range(3):
            print("{0} | {1} | {2} ".format(" ".join(str(l) for l in kartka[c][0:3]),
                                            " ".join(str(l) for l in kartka[c][3:6]),
                                            " ".join(str(l) for l in kartka[c][6:9])))
            c += 1
        if _ != 2:
            print("------+-------+-------")

def AI():
    add = [_ for _ in range(1, 10)]
    for x in range(9):
        for _ in range(9):
            if kartka[x][_] == ".":
                kartka[x][_] = add[:]

    while sum([sum([isinstance(x, list) for x in _]) for _ in kartka]) != 0:
        cop = 0
        for x in range(0, 9):
            for y in range(0, 9):
                if type(kartka[x][y]) is list:
                    if len(kartka[x][y]) == 1:
                        kartka[x][y] = kartka[x][y][0]

        for n in range(1, 10):
            for l in range(1, 10):
                c = Okna(n, kartka)
                ok = []
                for _ in c:
                    ok += _
                if l in ok:
                    for _ in range(9):
                        if type(ok[_]) is list:
                            if l in ok[_]:
                                del ok[_][ok[_].index(l)]
                                cop += 1
                                if len(ok[_]) == 1:
                                    ok[_] = ok[_][0]
                up = []
                for x in range(0, 7, 3):
                    up += [ok[x: x + 3]]
                UpOkna(n, up)

        for n in range(9):
            for l in range(1, 10):
                if l in kartka[n]:
                    for _ in range(9):
                        if type(kartka[n][_]) is list:
                            if l in kartka[n][_]:
                                del kartka[n][_][kartka[n][_].index(l)]
                                cop += 1
                                if len(kartka[n][_]) == 1:
                                    kartka[n][_] = kartka[n][_][0]

        for n in range(1, 10):
            for l in range(1, 10):
                ciag = Pion(n)
                if l in ciag:
                    for _ in range(9):
                        if type(ciag[_]) is list:
                            if l in ciag[_]:
                                del ciag[_][ciag[_].index(l)]
                                cop += 1
                                if len(ciag[_]) == 1:
                                    ciag[_] = ciag[_][0]
                UpPion(n, ciag)

        if cop == 0:
            coop = 0
            for n in range(9):
                inde = []
                spr = []
                fin = []
                c = 0
                for x in range(9):
                    if type(kartka[n][x]) is list:
                        inde.append(x)
                        spr += kartka[n][x]
                        c += 1
                if c > 1:
                    for l in range(1, 10):
                        if spr.count(l) == 1:
                            fin.append(l)
                for x in inde:
                    for j in fin:
                        if j in kartka[n][x]:
                            kartka[n][x] = j
                            coop += 1
                            break

            if coop == 0:
                for n in range(1, 10):
                    c = Okna(n, kartka)
                    ciag = []
                    for _ in c:
                        ciag += _
                    inde = []
                    spr = []
                    fin = []
                    c = 0
                    for x in range(9):
                        if type(ciag[x]) is list:
                            inde.append(x)
                            spr += ciag[x]
                            c += 1
                    if c > 1:
                        for l in range(1, 10):
                            if spr.count(l) == 1:
                                fin.append(l)
                    for x in inde:
                        for j in fin:
                            if j in ciag[x]:
                                ciag[x] = j
                                coop += 1
                                break
                    up = []
                    for x in range(0, 7, 3):
                        up += [ciag[x: x + 3]]
                    UpOkna(n, up)

            if coop == 0:
                for n in range(1, 10):
                    ciag = Pion(n)
                    inde = []
                    spr = []
                    fin = []
                    c = 0
                    for x in range(9):
                        if type(ciag[x]) is list:
                            inde.append(x)
                            spr += ciag[x]
                            c += 1
                    if c > 1:
                        for l in range(1, 10):
                            if spr.count(l) == 1:
                                fin.append(l)
                    for x in inde:
                        for j in fin:
                            if j in ciag[x]:
                                ciag[x] = j
                                coop += 1
                                break
                    UpPion(n, ciag)
            # -----------------------
            # Metoda Identycznych Par
            # -----------------------
            if coop == 0:
                for nmr in range(0, 9):
                    spr = kartka[nmr]

                    listinspr = 0
                    for x in spr:
                        if type(x) == list:
                            listinspr += 1
                    for n, chk in enumerate(spr):
                        if chk in reversed(sorted([x for x in spr if type(x) != int and len(x) <= listinspr], key=len)):
                            takiesame = [n]
                            for i, spr_lista in enumerate(spr):
                                if type(spr_lista) is not int and len(spr_lista) <= len(chk) and i != n:
                                    for liczba in spr_lista:
                                        if liczba in chk:
                                            if i not in takiesame:
                                                takiesame.append(i)
                                        else:
                                            if i in takiesame:
                                                del takiesame[takiesame.index(i)]
                                            break
                            glowna = sorted(spr[takiesame[0]])
                            reszta = []
                            for _ in takiesame[1:]:
                                reszta += spr[_]
                            reszta = sorted(list(set(reszta)))
                            if reszta == glowna and len(takiesame) == len(glowna):
                                nowa = copy.deepcopy(spr)
                                for i, spr_lista in enumerate(nowa):
                                    if i not in takiesame and type(spr_lista) is not int:
                                        for liczba in glowna:
                                            if liczba in spr_lista:
                                                del spr_lista[spr_lista.index(liczba)]
                                czynowa = kartka[nmr]
                                if czynowa != nowa:
                                    kartka[nmr] = nowa
                                    coop += 1
                                    break

            if coop == 0:
                for nmr in range(1, 10):
                    spr = Pion(nmr)

                    listinspr = 0
                    for x in spr:
                        if type(x) == list:
                            listinspr += 1
                    for n, chk in enumerate(spr):
                        if chk in reversed(sorted([x for x in spr if type(x) != int and len(x) <= listinspr], key=len)):
                            takiesame = [n]
                            for i, spr_lista in enumerate(spr):
                                if type(spr_lista) is not int and len(spr_lista) <= len(chk) and i != n:
                                    for liczba in spr_lista:
                                        if liczba in chk:
                                            if i not in takiesame:
                                                takiesame.append(i)
                                        else:
                                            if i in takiesame:
                                                del takiesame[takiesame.index(i)]
                                            break
                            glowna = sorted(spr[takiesame[0]])
                            reszta = []
                            for _ in takiesame[1:]:
                                reszta += spr[_]
                            reszta = sorted(list(set(reszta)))
                            if reszta == glowna and len(takiesame) == len(glowna):
                                nowa = copy.deepcopy(spr)
                                for i, spr_lista in enumerate(nowa):
                                    if i not in takiesame and type(spr_lista) is not int:
                                        for liczba in glowna:
                                            if liczba in spr_lista:
                                                del spr_lista[spr_lista.index(liczba)]
                                czynowa = Pion(nmr)
                                if czynowa != nowa:
                                    UpPion(nmr, nowa)
                                    coop += 1
                                    break

            if coop == 0:
                for nmr in range(1, 10):
                    sprrrr = Okna(nmr, kartka)
                    spr = []
                    for _ in sprrrr:
                        spr += _

                    listinspr = 0
                    for x in spr:
                        if type(x) == list:
                            listinspr += 1
                    for n, chk in enumerate(spr):
                        if chk in reversed(sorted([x for x in spr if type(x) != int and len(x) <= listinspr], key=len)):
                            takiesame = [n]
                            for i, spr_lista in enumerate(spr):
                                if type(spr_lista) is not int and len(spr_lista) <= len(chk) and i != n:
                                    for liczba in spr_lista:
                                        if liczba in chk:
                                            if i not in takiesame:
                                                takiesame.append(i)
                                        else:
                                            if i in takiesame:
                                                del takiesame[takiesame.index(i)]
                                            break
                            glowna = sorted(spr[takiesame[0]])
                            reszta = []
                            for _ in takiesame[1:]:
                                reszta += spr[_]
                            reszta = sorted(list(set(reszta)))
                            if reszta == glowna and len(takiesame) == len(glowna):
                                nowa = copy.deepcopy(spr)
                                for i, spr_lista in enumerate(nowa):
                                    if i not in takiesame and type(spr_lista) is not int:
                                        for liczba in glowna:
                                            if liczba in spr_lista:
                                                del spr_lista[spr_lista.index(liczba)]
                                czynowaaaa = Okna(nmr, kartka)
                                czynowa = []
                                for _ in czynowaaaa:
                                    czynowa += _

                                if czynowa != nowa:
                                    up = []
                                    for x in range(0, 7, 3):
                                        up += [nowa[x: x + 3]]
                                    UpOkna(nmr, up)
                                    coop += 1
                                    break

            # -------------------
            # Metoda Ukrytych Par
            # -------------------

            if coop == 0:
                for nmr in range(1, 10):
                    spr = Pion(nmr)
                    ilejest = {}
                    for n, _ in enumerate(spr):
                        if type(_) is list:
                            for liczba in _:
                                try:
                                    ilejest[liczba].append(n)
                                except:
                                    ilejest[liczba] = [n]

                    for n, chk in ilejest.items():
                        takiesame = [n]
                        for i, spr_lista in ilejest.items():
                            if len(spr_lista) <= len(chk) and i != n:
                                for liczba in spr_lista:
                                    if liczba in chk:
                                        if i not in takiesame:
                                            takiesame.append(i)
                                    else:
                                        if i in takiesame:
                                            del takiesame[takiesame.index(i)]
                                        break
                        glowna = sorted(ilejest[takiesame[0]])
                        reszta = []
                        for _ in takiesame[1:]:
                            reszta += ilejest[_]
                        reszta = sorted(list(set(reszta)))
                        nowa = copy.deepcopy(spr)
                        if glowna == reszta and len(takiesame) == len(glowna):
                            for x in glowna:
                                for liczba in spr[x]:
                                    if liczba not in takiesame:
                                        del nowa[x][nowa[x].index(liczba)]
                        if nowa != spr:
                            UpPion(nmr, nowa)
                            coop += 1
                            break
            if coop == 0:
                for nmr in range(1, 10):
                    sprrr = Okna(nmr, kartka)
                    spr = []
                    for x in sprrr:
                        spr += x
                    ilejest = {}
                    for n, _ in enumerate(spr):
                        if type(_) is list:
                            for liczba in _:
                                try:
                                    ilejest[liczba].append(n)
                                except:
                                    ilejest[liczba] = [n]

                    for n, chk in ilejest.items():
                        takiesame = [n]
                        for i, spr_lista in ilejest.items():
                            if len(spr_lista) <= len(chk) and i != n:
                                for liczba in spr_lista:
                                    if liczba in chk:
                                        if i not in takiesame:
                                            takiesame.append(i)
                                    else:
                                        if i in takiesame:
                                            del takiesame[takiesame.index(i)]
                                        break
                        glowna = sorted(ilejest[takiesame[0]])
                        reszta = []
                        for _ in takiesame[1:]:
                            reszta += ilejest[_]
                        reszta = sorted(list(set(reszta)))
                        nowa = copy.deepcopy(spr)
                        if glowna == reszta and len(takiesame) == len(glowna):
                            for x in glowna:
                                for liczba in spr[x]:
                                    if liczba not in takiesame:
                                        del nowa[x][nowa[x].index(liczba)]
                        if nowa != spr:
                            up = []
                            for x in range(0, 3):
                                up.append(nowa[3 * x: 3 * x + 3])
                            UpOkna(nmr, up)
                            coop += 1
                            break

            # ---------------------------------
            # Metoda Par w Jednym Poziomie
            # Gdzie Nie ma Więcej w Oknie
            # 1 1 1 del 1 del 1 del 1 2 3 del 1
            # 2 2 2
            # 2 2 2
            # ---------------------------------
            if coop == 0:
                for x in range(0, 3):
                    for y in range(0, 9):
                        glowna = [_ for _ in kartka[y][3 * x: 3 * x + 3] if type(_) is list]
                        if glowna == []:
                            continue

                        pary = []
                        for listaspr in glowna:
                            spr = []
                            for _ in glowna:
                                spr += _
                            for liczbaspr in listaspr:
                                if 1 < spr.count(liczbaspr):
                                    if liczbaspr not in pary:
                                        pary.append(liczbaspr)

                        reszta = []
                        if y in range(0, 3):
                            for yr in range(0, 3):
                                if yr != y:
                                    reszta += kartka[yr][3 * x: 3 * x + 3]
                        if y in range(3, 6):
                            for yr in range(3, 6):
                                if yr != y:
                                    reszta += kartka[yr][3 * x: 3 * x + 3]
                        if y in range(6, 9):
                            for yr in range(6, 9):
                                if yr != y:
                                    reszta += kartka[yr][3 * x: 3 * x + 3]

                        finalreszta = []
                        for lista in reszta:
                            if type(lista) == list:
                                for liczba in lista:
                                    if liczba not in finalreszta:
                                        finalreszta.append(liczba)

                        wynik = []
                        for liczba in pary:
                            if liczba not in finalreszta:
                                wynik.append(liczba)
                        for _ in range(9):
                            if type(kartka[y][_]) == list and _ not in range(3 * x, 3 * x + 3):
                                for liczba in wynik:
                                    if liczba in kartka[y][_]:
                                        del kartka[y][_][kartka[y][_].index(liczba)]
                                        coop += 1

            # ---------------------------------
            # Metoda Par w Jednym Pionie
            # Gdzie Nie ma Więcej w Oknie
            # ---------------------------------

            if coop == 0:
                for x in range(0, 3):
                    for y in range(1, 10):
                        glowna = [_ for _ in Pion(y)[3 * x: 3 * x + 3] if type(_) is list]
                        if glowna == []:
                            continue

                        pary = []
                        for listaspr in glowna:
                            spr = []
                            for _ in glowna:
                                spr += _
                            for liczbaspr in listaspr:
                                if 1 < spr.count(liczbaspr):
                                    if liczbaspr not in pary:
                                        pary.append(liczbaspr)

                        reszta = []
                        if y in range(1, 4):
                            for yr in range(1, 4):
                                if yr != y:
                                    reszta += Pion(yr)[3 * x: 3 * x + 3]
                        if y in range(4, 7):
                            for yr in range(4, 7):
                                if yr != y:
                                    reszta += Pion(yr)[3 * x: 3 * x + 3]
                        if y in range(7, 10):
                            for yr in range(7, 10):
                                if yr != y:
                                    reszta += Pion(yr)[3 * x: 3 * x + 3]

                        finalreszta = []
                        for lista in reszta:
                            if type(lista) == list:
                                for liczba in lista:
                                    if liczba not in finalreszta:
                                        finalreszta.append(liczba)

                        wynik = []
                        for liczba in pary:
                            if liczba not in finalreszta:
                                wynik.append(liczba)
                        for _ in range(9):
                            if type(Pion(y)[_]) == list and _ not in range(3 * x, 3 * x + 3):
                                for liczba in wynik:
                                    if liczba in Pion(y)[_]:
                                        todel = Pion(y)
                                        del todel[_][todel[_].index(liczba)]
                                        UpPion(y, todel)
                                        coop += 1

            if coop == 0:
                break

def Game(lista):
    import pygame
    import copy
    global kartka
    kartka = copy.deepcopy(lista)
    pygame.font.init()
    screen = pygame.display.set_mode((500, 600))
    x = 0
    y = 0
    dif = 500 / 9
    val = 0
    c = -1
    z = 0
    sure = 0
    period = False
    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)
    font3 = pygame.font.SysFont("comicsans", 15)
    history = []
    roz = copy.deepcopy(kartka)
    AI()
    kartka, roz = roz, kartka
    if End(roz) is True:
        rodzaj = "normal"
    else:
        rodzaj = "again"


    pencilON = pygame.image.load("pencilON.png")
    pencilON = pygame.transform.scale(pencilON, (42, 42))
    pencilOFF = pygame.image.load("pencilOFF.png")
    pencilOFF = pygame.transform.scale(pencilOFF, (42, 42))

    def check():
        if rodzaj == "normal":
            for x in range(9):
                for xx in range(9):
                    if kartka[x][xx] != "." and type(kartka[x][xx]) != list and kartka[x][xx] != roz[x][xx]:
                        return False
        elif rodzaj == "again":
            if Bugs(kartka) is not True:
                return False

        return True

    def hint():
        global kartka
        if rodzaj == "normal":
            lista = []
            for x in range(9):
                for xx in range(9):
                    if kartka[x][xx] == ".":
                        lista.append((x, xx))
            var = random.choice(lista)
            kartka[var[0]][var[1]] = roz[var[0]][var[1]]
        else:
            return False

        return True

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (32, 201, 114), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (32, 201, 114), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    def draw_queue():
        for i in range(9):
            for j in range(9):
                if type(kartka[j][i]) == list:
                    for x in kartka[j][i]:
                        xx = 0
                        yy = 0
                        if x == 2:
                            xx = 17
                        elif x == 3:
                            xx = 34
                        elif x == 4:
                            yy = 17
                        elif x == 5:
                            xx = 17
                            yy = 17
                        elif x == 6:
                            xx = 34
                            yy = 17
                        elif x == 7:
                            yy = 34
                        elif x == 8:
                            xx = 17
                            yy = 34
                        elif x == 9:
                            xx = 34
                            yy = 34
                        if i in (2, 5, 8):
                            xx -= 1
                        if i in (0, 3, 6):
                            xx += 2
                        if j in (0, 3, 6):
                            yy += 1
                        if j in (2, 5, 8):
                            yy -= 1
                        text1 = font3.render(str(x), 1, (0, 0, 0))
                        screen.blit(text1, (i * dif + 6 + xx, j * dif + yy))

    def draw():
        for i in range(9):
            for j in range(9):
                if history != []:
                    if kartka[j][i] != "." and type(kartka[j][i]) != list:
                        pygame.draw.rect(screen, (255, 115, 0), (i * dif, j * dif, dif + 1, dif + 1))
                    if history[0][j][i] != "." and type(history[0][j][i]) != list:
                        pygame.draw.rect(screen, (222, 53, 53), (i * dif, j * dif, dif + 1, dif + 1))
                    if kartka[j][i] != "." and type(kartka[j][i]) != list:
                        text1 = font1.render(str(kartka[j][i]), 1, (0, 0, 0))
                        screen.blit(text1, (i * dif + 15, j * dif))
                else:
                    if kartka[j][i] != "." and type(kartka[j][i]) != list:
                        pygame.draw.rect(screen, (222, 53, 53), (i * dif, j * dif, dif + 1, dif + 1))
                        text1 = font1.render(str(kartka[j][i]), 1, (0, 0, 0))
                        screen.blit(text1, (i * dif + 15, j * dif))

        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    def raise_error1():
        if Bugs(kartka) is True:
            text1 = font1.render("No Contradiction", 1, (0, 0, 0))
        else:
            text1 = font2.render(str(Bugs(kartka)), 1, (0, 0, 0))
        screen.blit(text1, (20, 520))

    def raise_error2():
        if check() is True:
            text1 = font1.render("Everything is Correct :)", 1, (0, 0, 0))
        else:
            if Bugs(kartka) is True:
                text1 = font2.render("You did mistake even if everything looks fine", 1, (0, 0, 0))
            else:
                text1 = font2.render(str(Bugs(kartka)), 1, (0, 0, 0))
        screen.blit(text1, (20, 520))

    def raise_won():
        text1 = font1.render("CONGRATULATION", 1, (0, 0, 0))
        text2 = font2.render("Press Enter to continue", 1, (0, 0, 0))
        screen.blit(text1, (20, 510))
        screen.blit(text2, (20, 560))

    def raise_lose():
        text1 = font1.render("There's mistake :(", 1, (0, 0, 0))
        screen.blit(text1, (20, 510))
        text2 = font2.render("Press U to undo or R to restart", 1, (0, 0, 0))
        screen.blit(text2, (20, 560))

    def instruction():
        text1 = font2.render("U - Undo R - Reset C - Check H - Hint", 1, (0, 0, 0))
        text2 = font2.render("A - Complete I - Redo D - Deep Check", 1, (0, 0, 0))
        if period is True:
            screen.blit(pencilON, (440, 524))
        else:
            screen.blit(pencilOFF, (440, 524))
        screen.blit(text1, (20, 520))
        screen.blit(text2, (20, 540))

    end = False
    run = True
    while run:
        e = 0
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x - 1 > -1:
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if x + 1 < 9:
                        x += 1
                if event.key == pygame.K_UP:
                    if y - 1 > -1:
                        y -= 1
                if event.key == pygame.K_DOWN:
                    if y + 1 < 9:
                        y += 1
                if event.key == pygame.K_DELETE:
                    val = "DEL"
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = 9
                if event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    val = "ENTER"
                if event.key == pygame.K_PERIOD:
                    val = "PERIOD"
                if event.key == pygame.K_a:
                    val = "A"
                if event.key == pygame.K_c:
                    val = "C"
                if event.key == pygame.K_u:
                    val = "U"
                if event.key == pygame.K_r:
                    val = "R"
                if event.key == pygame.K_i:
                    val = "I"
                if event.key == pygame.K_d:
                    val = "D"
                if event.key == pygame.K_h:
                    val = "H"
                if event.key == pygame.K_y:
                    val = "Y"
                if event.key == pygame.K_n:
                    val = "N"
        if end is True:
            break
        if End(kartka) is True:
            raise_won()
            if val == "ENTER":
                break
            e = 1
        elif End(kartka) is False:
            raise_lose()
            e = 1
        if sure != 0:
            addtext = ""
            if sure == "H":
                addtext = "use hint"
            if sure == "D":
                addtext = "use deep hint"
            if sure == "R":
                addtext = "restart"
            if sure == "A":
                addtext = "complete"
            text1 = font2.render("Are you sure you want to {0}?".format(addtext), 1, (0, 0, 0))
            text2 = font2.render("n - No y - Yes", 1, (0, 0, 0))
            screen.blit(text1, (20, 520))
            screen.blit(text2, (20, 540))
            if val == "Y":
                sure += "Y"
            elif val == "N":
                sure = 0
            else:
                draw()
                draw_box()
                draw_queue()
                pygame.display.update()
                continue
        if val in range(1, 10):
            if period is False:
                if history == []:
                    if kartka[int(y)][int(x)] == ".":
                        del history[c + 1:]
                        history.append(copy.deepcopy(kartka))
                        c += 1
                        z = 0
                        sure = 0
                        kartka[int(y)][int(x)] = val
                else:
                    if history[0][int(y)][int(x)] == ".":
                        del history[c + 1:]
                        history.append(copy.deepcopy(kartka))
                        c += 1
                        z = 0
                        sure = 0
                        kartka[int(y)][int(x)] = val
            else:
                if history == []:
                    if kartka[int(y)][int(x)] == ".":
                        if type(kartka[int(y)][int(x)]) != list:
                            del history[c + 1:]
                            history.append(copy.deepcopy(kartka))
                            c += 1
                            z = 0
                            sure = 0
                            kartka[int(y)][int(x)] = [val]
                        elif type(kartka[int(y)][int(x)]) == list:
                            if val not in kartka[int(y)][int(x)]:
                                del history[c + 1:]
                                history.append(copy.deepcopy(kartka))
                                c += 1
                                z = 0
                                sure = 0
                                kartka[int(y)][int(x)].append(val)
                            elif val in kartka[int(y)][int(x)]:
                                del history[c + 1:]
                                history.append(copy.deepcopy(kartka))
                                c += 1
                                z = 0
                                sure = 0
                                del kartka[int(y)][int(x)][kartka[int(y)][int(x)].index(val)]
                else:
                    if type(history[0][int(y)][int(x)]) != int:
                        if type(kartka[int(y)][int(x)]) != list:
                            del history[c + 1:]
                            history.append(copy.deepcopy(kartka))
                            c += 1
                            z = 0
                            sure = 0
                            kartka[int(y)][int(x)] = [val]
                        elif type(kartka[int(y)][int(x)]) == list:
                            if val not in kartka[int(y)][int(x)]:
                                del history[c + 1:]
                                history.append(copy.deepcopy(kartka))
                                c += 1
                                z = 0
                                sure = 0
                                kartka[int(y)][int(x)].append(val)
                            elif val in kartka[int(y)][int(x)]:
                                del history[c + 1:]
                                history.append(copy.deepcopy(kartka))
                                c += 1
                                z = 0
                                sure = 0
                                del kartka[int(y)][int(x)][kartka[int(y)][int(x)].index(val)]
            val = 0
        elif val == "DEL":
            if history[0][int(y)][int(x)] == "." and history != []:
                del history[c + 1:]
                history.append(copy.deepcopy(kartka))
                c += 1
                z = 0
                sure = 0
                kartka[int(y)][int(x)] = "."
            val = 0
        elif val == "PERIOD":
            if period is True:
                period = False
            else:
                period = True
            val = 0
        elif val == "A" or sure == "AY" or val == "AP":
            if sure == "AY" or val == "AP":
                if check() is True:
                    del history[c + 1:]
                    history.append(copy.deepcopy(kartka))
                    c += 1
                    val = 0
                    z = 0
                    for x in range(9):
                        for y in range(9):
                            if type(kartka[x][y]) == list:
                                kartka[x][y] = "."
                    AI()
                else:
                    if Bugs(kartka) is True:
                        text1 = font2.render("You did mistake even if everything looks fine", 1, (0, 0, 0))
                    else:
                        text1 = font2.render(str(Bugs(kartka)), 1, (0, 0, 0))
                    screen.blit(text1, (20, 520))
                    val = "AP"
                sure = 0
            else:
                sure = "A"
        elif val == "C":
            # to del it's only to testing purpose
            print(kartka)
            val = 0
            # to del it's only to testing purpose
            raise_error1()
        elif val == "D"  or sure == "DY" or val == "DP":
            if sure == "DY" or val == "DP":
                if rodzaj == "normal":
                    raise_error2()
                else:
                    text1 = font2.render("We're working at that case scenario", 1, (0, 0, 0))
                    screen.blit(text1, (20, 520))
                val = "DP"
                sure = 0
            else:
                sure = "D"
        elif val == "H" or sure == "HY" or val == "HP":
            if sure == "HY" or val == "HP":
                if check() is True and val != "HP":
                    del history[c + 1:]
                    history.append(copy.deepcopy(kartka))
                    c += 1
                    val = 0
                    z = 0
                    hint()
                    if hint() is False:
                        val = "HP"
                else:
                    if hint() is False:
                        text1 = font2.render("We're working at that case scenario", 1, (0, 0, 0))
                    elif Bugs(kartka) is True:
                        text1 = font2.render("You did mistake even if everything looks fine", 1, (0, 0, 0))
                    else:
                        text1 = font2.render(str(Bugs(kartka)), 1, (0, 0, 0))
                    screen.blit(text1, (20, 520))
                    val = "HP"
                sure = 0
            else:
                sure = "H"
        elif val == "U":
            if history and c > -1:
                if z == 0:
                    history.append(copy.deepcopy(kartka))
                z = 1
                kartka = history[c]
                c -= 1
                val = 0
            instruction()
        elif val == "R" or sure == "RY":
            if sure == "RY":
                if history:
                    kartka = history[0]
                    c = -1
                    history = []
                instruction()
                sure = 0
            else:
                sure = "R"
        elif val == "I":
            if c < len(history) - 2:
                c += 1
                kartka = history[c + 1]
            val = 0
        else:
            if e == 0:
                instruction()
        draw()
        draw_box()
        draw_queue()
        pygame.display.update()
    pygame.quit()

def Add():
    import pygame
    import copy
    global kartka
    kartka = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    pygame.font.init()
    screen = pygame.display.set_mode((500, 600))
    x = 0
    y = 0
    dif = 500 / 9
    val = 0
    c = -1
    sure = 0
    font1 = pygame.font.SysFont("comicsans", 40)
    font2 = pygame.font.SysFont("comicsans", 20)
    history = []

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (32, 201, 114), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(screen, (32, 201, 114), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    def draw():
        for i in range(9):
            for j in range(9):
                    if kartka[j][i] != ".":
                        pygame.draw.rect(screen, (222, 53, 53), (i * dif, j * dif, dif + 1, dif + 1))
                        text1 = font1.render(str(kartka[j][i]), 1, (0, 0, 0))
                        screen.blit(text1, (i * dif + 15, j * dif + 5))

        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    def instruction():
        text1 = font2.render("R - Reset", 1, (0, 0, 0))
        text2 = font2.render("Enter - Save and Quit", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))
        screen.blit(text2, (20, 540))

    def crypt(lista):
        out = ""
        for x in range(9):
            t = [str(_) for _ in lista[x]]
            out += " ".join(t) + " "
        return out

    end = False
    run = True
    while run:
        e = 0
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x - 1 > -1:
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if x + 1 < 9:
                        x += 1
                if event.key == pygame.K_UP:
                    if y - 1 > -1:
                        y -= 1
                if event.key == pygame.K_DOWN:
                    if y + 1 < 9:
                        y += 1
                if event.key == pygame.K_DELETE:
                    val = "DEL"
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = 9
                if event.key == pygame.K_r:
                    val = "R"
                if event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    val = "ENTER"
                if event.key == pygame.K_y:
                    val = "Y"
                if event.key == pygame.K_n:
                    val = "N"
        if end is True:
            break
        if sure != 0:
            addtext = ""
            if sure == "R":
                addtext = "Are you sure you want to restart"
            if sure == "ENTER":
                addtext = "Are tou sure you've done and you want to save and exit"
            text1 = font2.render("{0}?".format(addtext), 1, (0, 0, 0))
            text2 = font2.render("n - No y - Yes", 1, (0, 0, 0))
            screen.blit(text1, (20, 520))
            screen.blit(text2, (20, 540))
            if val == "Y":
                sure += "Y"
            elif val == "N":
                sure = 0
            else:
                draw()
                draw_box()
                pygame.display.update()
                continue
        if val == "ENTER" or sure == "ENTERY":
            if sure == "ENTERY":
                import sqlite3
                base = sqlite3.connect('sudoku.db')
                do = base.cursor()
                do.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL);''')
                do.execute('''INSERT INTO sheets (name) VALUES (?);''', (crypt(kartka), ))
                base.commit()
                base.close()
                break
            else:
                sure = "ENTER"
        if val in range(1, 10):
            spr = copy.deepcopy(kartka)
            spr[int(y)][int(x)] = val
            if Bugs(spr) is True:
                del history[c + 1:]
                history.append(copy.deepcopy(kartka))
                c += 1
                kartka[int(y)][int(x)] = val
                val = 0
            else:
                val = 0
        elif val == "DEL":
            history.append(copy.deepcopy(kartka))
            c += 1
            kartka[int(y)][int(x)] = "."
            val = 0
        elif val == "R" or sure == "RY":
            if sure == "RY":
                if history:
                    kartka = history[0]
                    c = -1
                    history = []
                instruction()
                sure = 0
            else:
                sure = "R"
        else:
            if e == 0:
                instruction()
        draw()
        draw_box()
        pygame.display.update()
    pygame.quit()
