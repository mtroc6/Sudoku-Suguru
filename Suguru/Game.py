import copy
liczby = []


def Display(linie, okna, liczby):
    import pygame
    for x in okna:
        okno = []
        index = []
        for i in x:
            okno.append(liczby[i[1]][i[0]])
            index.append((i[1], i[0]))
        for n, liczba in enumerate(okno):
            if type(liczba) == str:
                liczby[index[n][0]][index[n][1]] = []
    period = False
    val = 0
    x = 0
    y = 0
    width = len(liczby[0])
    height = len(liczby)
    screen = pygame.display.set_mode((width * 60 + 3, height * 60 + 100))
    pygame.font.init()
    font1 = pygame.font.SysFont("comicsans", 40)
    font3 = pygame.font.SysFont("comicsans", 15)

    pencilON = pygame.image.load("pencilON.png")
    pencilON = pygame.transform.scale(pencilON, (42, 42))
    pencilOFF = pygame.image.load("pencilOFF.png")
    pencilOFF = pygame.transform.scale(pencilOFF, (42, 42))

    def Bugs():
        for x in okna:
            okno = []
            for i in x:
                okno.append(liczby[i[1]][i[0]])
            for liczba in okno:
                if type(liczba) == int:
                    if liczba > len(okno):
                        return False
                    if okno.count(liczba) > 1:
                        return False

        for j in range(height):
            for i in range(width):
                if type(liczby[j][i]) == int:
                    for y_spr in range(3):
                        for x_spr in range(3):
                            if y_spr == 1 and x_spr == 1:
                                continue
                            if y_spr + j - 1 >= height or y_spr + j - 1 < 0 or x_spr + i - 1 >= width or x_spr + i - 1 < 0:
                                continue
                            if type(liczby[y_spr + j - 1][x_spr + i - 1]) == int:
                                if liczby[j][i] == liczby[y_spr + j - 1][x_spr + i - 1]:
                                    return False

        return True

    def Win():
        for x in liczby:
            for _ in x:
                if type(_) == list:
                    return False

        if Bugs() is False:
            return False

        return True

    def AI():
        # Dodawanie liczb ołówkiem
        for x in okna:
            okno = []
            index = []
            for i in x:
                okno.append(liczby[i[1]][i[0]])
                index.append((i[1], i[0]))
            add = []
            for szukana in range(1, len(okno) + 1):
                if szukana not in okno:
                    add.append(szukana)
            for n, liczba in enumerate(okno):
                if type(liczba) == list:
                    liczby[index[n][0]][index[n][1]] = add[:]

        while True:
            coop = 0
            # Dodawanie Jednej Liczby w Oknie
            if coop == 0:
                for x in okna:
                    okno = []
                    index = []
                    for i in x:
                        okno.append(liczby[i[1]][i[0]])
                        index.append((i[1], i[0]))
                    for n, liczba in enumerate(okno):
                        if type(liczba) == list:
                            if len(liczba) == 1:
                                liczby[index[n][0]][index[n][1]] = liczby[index[n][0]][index[n][1]][0]
                                coop += 1

            # Usuwanie Liczby Dookoła
            if coop == 0:
                for j in range(height):
                    for i in range(width):
                        if type(liczby[j][i]) == int:
                            for y_spr in range(3):
                                for x_spr in range(3):
                                    if y_spr == 1 and x_spr == 1:
                                        continue
                                    if y_spr + j - 1 >= height or y_spr + j - 1 < 0 or x_spr + i - 1 >= width or x_spr + i - 1 < 0:
                                        continue
                                    if type(liczby[y_spr + j - 1][x_spr + i - 1]) == list:
                                        if liczby[j][i] in liczby[y_spr + j - 1][x_spr + i - 1]:
                                            del liczby[y_spr + j - 1][x_spr + i - 1][liczby[y_spr + j - 1][x_spr + i - 1].index(liczby[j][i])]
                                            coop += 1

            # Usuwanie Ołówków Dodanych liczb w oknie
            if coop == 0:
                for x in okna:
                    okno = []
                    index = []
                    for i in x:
                        okno.append(liczby[i[1]][i[0]])
                        index.append((i[1], i[0]))
                    add = []
                    for szukana in range(1, len(okno) + 1):
                        if szukana in okno:
                            add.append(szukana)
                    for i, _ in enumerate(okno):
                        if type(_) == list:
                            for liczba in add:
                                if liczba in _:
                                    del liczby[index[i][0]][index[i][1]][liczby[index[i][0]][index[i][1]].index(liczba)]
                                    coop += 1

            # HIDDEN ONE możliwe że potem do usunięcia jak będzie wiecej HIDDEN
            if coop == 0:
                for x in okna:
                    okno = []
                    index = []
                    for i in x:
                        okno.append(liczby[i[1]][i[0]])
                        index.append((i[1], i[0]))
                    all = []
                    for _ in okno:
                        if type(_) == list:
                            all += _
                    for i, _ in enumerate(okno):
                        if type(_) == list:
                            for czy in _:
                                if all.count(czy) == 1:
                                    liczby[index[i][0]][index[i][1]] = czy
                                    coop += 1
            # Szukanie Części Wspólnej Par
            if coop == 0:
                for nmr in okna:
                    ilejest = {}
                    for _ in nmr:
                        if type(liczby[_[1]][_[0]]) is list:
                            for liczba in liczby[_[1]][_[0]]:
                                try:
                                    ilejest[liczba].append((_[1], _[0]))
                                except:
                                    ilejest[liczba] = [(_[1], _[0])]
                    # Część Wspólna
                    for liczba, glowneindexy in ilejest.items():
                        radius = []
                        for glownyindex in glowneindexy:
                            for y_spr in range(3):
                                for x_spr in range(3):
                                    if y_spr == 1 and x_spr == 1:
                                        continue
                                    if y_spr + glownyindex[0] - 1 >= height or y_spr + glownyindex[0] - 1 < 0 or x_spr + \
                                            glownyindex[1] - 1 >= width or x_spr + glownyindex[1] - 1 < 0:
                                        continue
                                    if type(liczby[y_spr + glownyindex[0] - 1][x_spr + glownyindex[1] - 1]) == list:
                                        if (y_spr + glownyindex[0] - 1, x_spr + glownyindex[1] - 1) not in glowneindexy and (
                                                x_spr + glownyindex[1] - 1, y_spr + glownyindex[0] - 1) not in nmr:
                                            radius.append((y_spr + glownyindex[0] - 1, x_spr + glownyindex[1] - 1))
                        # Usuwanie Ołówka z Części wspólnej
                        for index in list(set(radius)):
                            if radius.count(index) == len(glowneindexy):
                                if liczba in liczby[index[0]][index[1]]:
                                    del liczby[index[0]][index[1]][liczby[index[0]][index[1]].index(liczba)]
                                    coop += 1
            # UKRYTE PARY
            # if coop == 0:
            #     for nmr in okna:
            #         ilejest = {}
            #         for n, _ in enumerate(nmr):
            #             if type(liczby[_[1]][_[0]]) is list:
            #                 for liczba in liczby[_[1]][_[0]]:
            #                     try:
            #                         ilejest[liczba].append((_[1], _[0]))
            #                     except:
            #                         ilejest[liczba] = [(_[1], _[0])]

            # Dla odległych samotnych okien musi być w danym miejscu liczba by było logiczne
            if coop == 0:
                if Win() is False:
                    for nmr in okna:
                        ilejest = {}
                        for _ in nmr:
                            if type(liczby[_[1]][_[0]]) is list:
                                for liczba in liczby[_[1]][_[0]]:
                                    try:
                                        ilejest[liczba].append((_[1], _[0]))
                                    except:
                                        ilejest[liczba] = [(_[1], _[0])]
                        # Część Wspólna
                        for liczba, glowneindexy in ilejest.items():
                            radiusglowny = []
                            for glownyindex in glowneindexy:
                                for y_spr in range(3):
                                    for x_spr in range(3):
                                        if y_spr == 1 and x_spr == 1:
                                            continue
                                        if y_spr + glownyindex[0] - 1 >= height or y_spr + glownyindex[
                                            0] - 1 < 0 or x_spr + \
                                                glownyindex[1] - 1 >= width or x_spr + glownyindex[1] - 1 < 0:
                                            continue
                                        if type(liczby[y_spr + glownyindex[0] - 1][x_spr + glownyindex[1] - 1]) == list:
                                            if (y_spr + glownyindex[0] - 1,
                                                x_spr + glownyindex[1] - 1) not in glowneindexy and (
                                                    x_spr + glownyindex[1] - 1, y_spr + glownyindex[0] - 1) not in nmr:
                                                radiusglowny.append((y_spr + glownyindex[0] - 1, x_spr + glownyindex[1] - 1))
                            radiusreszta = []
                            for nmrr in okna:
                                if nmrr == nmr:
                                    continue
                                ilejest = {}
                                for _ in nmrr:
                                    if type(liczby[_[1]][_[0]]) is list:
                                        for liczba in liczby[_[1]][_[0]]:
                                            try:
                                                ilejest[liczba].append((_[1], _[0]))
                                            except:
                                                ilejest[liczba] = [(_[1], _[0])]
                                # Część Wspólna
                                for liczba, glowneindexy in ilejest.items():

                                    for glownyindex in glowneindexy:
                                        for y_spr in range(3):
                                            for x_spr in range(3):
                                                if y_spr == 1 and x_spr == 1:
                                                    continue
                                                if y_spr + glownyindex[0] - 1 >= height or y_spr + glownyindex[
                                                    0] - 1 < 0 or x_spr + \
                                                        glownyindex[1] - 1 >= width or x_spr + glownyindex[1] - 1 < 0:
                                                    continue
                                                if type(liczby[y_spr + glownyindex[0] - 1][
                                                            x_spr + glownyindex[1] - 1]) == list:
                                                    if (y_spr + glownyindex[0] - 1,
                                                        x_spr + glownyindex[1] - 1) not in glowneindexy and (
                                                            x_spr + glownyindex[1] - 1,
                                                            y_spr + glownyindex[0] - 1) not in nmr:
                                                        radiusreszta.append(
                                                            (y_spr + glownyindex[0] - 1, x_spr + glownyindex[1] - 1))
                            c = 0
                            for radius in radiusglowny:
                                if radius in radiusreszta:
                                    c += 1

                            if c == 1:
                                for radius in radiusglowny:
                                    if radius in radiusreszta:
                                        liczby[radius[0]][radius[1]] = liczba
                                        coop += 1
            # Backtracking ???
            # if coop == 0:
            #     for nmr in sorted(okna, key=len):
            #         for _ in nmr:
            #             pass
            #             if type(liczby[_[1]][_[0]]) is list:
            #                 for x in liczby[_[1]][_[0]]:
            #                     new = copy.deepcopy(liczby)
            #                     liczby[_[1]][_[0]] = x
            #                     AI()
            #                     if Win() is True:
            #                         coop += 1
            #                         break
            #                     else:
            #                         liczby, new = new, liczby

            if coop == 0:
                break

    def draw_queue():
        for j in range(height):
            for i in range(width):
                if type(liczby[j][i]) == list:
                    for x in liczby[j][i]:
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
                        text1 = font3.render(str(x), 1, (0, 0, 0))
                        screen.blit(text1, (i * 60 + 6 + xx, j * 60 + yy))

    def draw_box():
        for i in range(2):
            pygame.draw.line(screen, (32, 201, 114), (x * 60 - 3, (y + i) * 60), (x * 60 + 60 + 3, (y + i) * 60), 7)
            pygame.draw.line(screen, (32, 201, 114), ((x + i) * 60, y * 60), ((x + i) * 60, y * 60 + 60), 7)


    def draw():
        for i in range(height + 1):
            if i == 0 or i == height:
                thick = 6
            else:
                thick = 1

            pygame.draw.line(screen, (0, 0, 0), (0, i * 60), (60 * width + 3, i * 60), thick)
        for i in range(width + 1):
            if i == 0 or i == width:
                thick = 6
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (i * 60, 0), (i * 60, 60 * height), thick)

        for line in linie:
            if line[0] % 2 == 0:
                pygame.draw.line(screen, (0, 0, 0), (line[0] * 60 // 2, line[1] * 60 // 2),
                                 (line[0] * 60 // 2, (line[1] + 2) * 60 // 2),
                                 6)
            else:
                pygame.draw.line(screen, (0, 0, 0), ((line[0] - 1) * 60 // 2 - 2, (line[1] + 1) * 60 // 2),
                                 ((line[0] + 1) * 60 // 2 + 3, (line[1] + 1) * 60 // 2), 6)

        for j in range(height):
            for i in range(width):
                if liczby[j][i] != "." and type(liczby[j][i]) != list:
                    text1 = font1.render(str(liczby[j][i]), 1, (0, 0, 0))
                    screen.blit(text1, (i * 60 + 15, j * 60))

    run = True
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_DELETE:
                    val = "DEL"
                if event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    val = "ENTER"
                if event.key == pygame.K_LEFT:
                    if x - 1 > -1:
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if x + 1 < width:
                        x += 1
                if event.key == pygame.K_UP:
                    if y - 1 > -1:
                        y -= 1
                if event.key == pygame.K_DOWN:
                    if y + 1 < height:
                        y += 1
                if event.key == pygame.K_a:
                    val = "A"
                if event.key == pygame.K_PERIOD:
                    if period is False:
                        period = True
                    else:
                        period = False

        if Win() is True:
            text1 = font1.render("That's End...", 1, (0, 0, 0))
            screen.blit(text1, (80, height * 60 + 20))
            if val == "ENTER":
                break

        if val in range(1, 10):
            if period is False:
                liczby[y][x] = val
                val = 0
            else:
                if val not in liczby[y][x]:
                    liczby[y][x].append(val)
                    val = 0
                else:
                    del liczby[y][x][liczby[y][x].index(val)]
                    val = 0


        if val == "A":
            AI()
            val = 0

        if val == "DEL":
            liczby[y][x] = []
            val = 0

        if Bugs() is False:
            text1 = font1.render("That's Illegal", 1, (0, 0, 0))
            screen.blit(text1, (20 , height * 60 + 20))

        if period is True:
            screen.blit(pencilON, (20, height * 60 + 28))
        else:
            screen.blit(pencilOFF, (20, height * 60 + 28))

        draw()
        draw_box()
        draw_queue()
        pygame.display.update()
    pygame.quit()
