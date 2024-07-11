def Display():
    import pygame
    pygame.font.init()
    font1 = pygame.font.SysFont("comicsans", 40)
    linie = []
    liczby = []
    okna = []
    okno = []
    dodane = []
    height = ""
    width = ""
    witch = 0
    x = 1
    y = 1
    val = None
    etap = 0

    def crypt(liniee, oknaa, liczbyy):
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

    run = True
    while run:
        screen = pygame.display.set_mode((900, 600))
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    val = "DEL"
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    val = "0"
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    val = "1"
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    val = "2"
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    val = "3"
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    val = "4"
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    val = "5"
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    val = "6"
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    val = "7"
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    val = "8"
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    val = "9"
                if event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    if witch == 0:
                        if len(width) != 0:
                            witch += 1
                    if witch == 1:
                        if len(height) != 0:
                            witch += 1

        if witch == 0:
            if val == "DEL":
                if len(width) > 0:
                    width = width[:-1]
            elif val is not None:
                 width += val
            val = None

        if witch == 1:
            if val == "DEL":
                if len(height) > 0:
                    height = height[:-1]
            elif val is not None:
                 height += val
            val = None

        if witch == 2:
            width = int(width)
            height = int(height)
            if height > 10:
                height = 10
            if width > 15:
                width = 15
            run = False

        text1 = font1.render("Width: {0}".format(width), 1, (0, 0, 0))
        text2 = font1.render("Height: {0}".format(height), 1, (0, 0, 0))
        screen.blit(text1, (300 , 100))
        screen.blit(text2, (300, 200))

        pygame.display.update()

    def Is_added():
        for j in range(height):
            for i in range(width):
                if dodane[j][i] == ".":
                    return False
        return True

    def draw_dodane():
        for j in range(height):
            for i in range(width):
                    if dodane[j][i] != ".":
                        pygame.draw.rect(screen, (222, 53, 53), (i * 60, j * 60, 60 + 1, 60 + 1))

    def draw_line():
        if x % 2 == 0:
            pygame.draw.line(screen, (12, 231, 242), (x * 60 // 2, y * 60 // 2), (x  * 60 // 2, (y + 2) * 60 // 2), 6)
        else:
            pygame.draw.line(screen, (12, 231, 242), ((x - 1) * 60 // 2, (y + 1) * 60 // 2), ((x + 1) * 60 // 2, (y + 1) * 60 // 2), 6)

    def draw_liczby():
        for j in range(height):
            for i in range(width):
                if liczby[j][i] != "." and type(liczby[j][i]) != list:
                    text1 = font1.render(str(liczby[j][i]), 1, (0, 0, 0))
                    screen.blit(text1, (i * 60 + 15, j * 60))

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
                pygame.draw.line(screen, (0, 0, 0), (line[0] * 60 // 2, line[1] * 60 // 2), (line[0] * 60 // 2, (line[1] + 2) * 60 // 2),
                                 6)
            else:
                pygame.draw.line(screen, (0, 0, 0), ((line[0] - 1) * 60 // 2 - 2, (line[1] + 1) * 60 // 2),
                                 ((line[0] + 1) * 60 // 2 + 3, (line[1] + 1) * 60 // 2), 6)
    pygame.quit()
    import pygame
    pygame.font.init()
    font1 = pygame.font.SysFont("comicsans", 40)
    run = True
    screen = pygame.display.set_mode((width * 60 + 3, height * 60 + 100))
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
                if event.key == pygame.K_LEFT:
                    if etap == 0:
                        if y == height * 2 - 2:
                            if x - 2 > 0:
                                x -= 2
                        elif x - 1 > 0:
                            x -= 1
                            if x % 2 == 0:
                                y -= 1
                            else:
                                y += 1
                    else:
                        if x - 1 > -1:
                            x -= 1
                if event.key == pygame.K_RIGHT:
                    if etap == 0:
                        if y == height * 2 - 2:
                            if x + 2 > 0:
                                x += 2
                        elif x + 1 < width * 2:
                            x += 1
                            if x % 2 == 0:
                                y -= 1
                            else:
                                y += 1
                    else:
                        if x + 1 < width:
                            x += 1
                if event.key == pygame.K_UP:
                    if etap == 0:
                        if y - 1 > 0:
                            y -= 2
                    else:
                        if y - 1 > -1:
                            y -= 1
                if event.key == pygame.K_DOWN:
                    if etap == 0:
                        if y + 1 < height * 2 - 2:
                            y += 2
                    else:
                        if y + 1 < height:
                            y += 1
                if event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    val = "ENTER"
                if event.key == pygame.K_s:
                    if etap == 2:
                        import sqlite3
                        base = sqlite3.connect('suguru.db')
                        do = base.cursor()
                        do.execute('''CREATE TABLE IF NOT EXISTS sheets (id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL);''')
                        do.execute('''INSERT INTO sheets (name) VALUES (?);''', (crypt(linie, okna, liczby),))
                        base.commit()
                        base.close()
                        run = False
                        etap += 1
                        break
                    if etap == 1:
                        if Is_added() is True:
                            okna.append(okno)
                            etap += 1
                            x = 0
                            y = 0
                            for j in range(height):
                                liczby.append(["." for _ in range(width)])
                        else:
                            okna.append(okno)
                            okno = []
                    if etap == 0:
                        etap += 1
                        x = 0
                        y = 0
                        for j in range(height):
                            dodane.append(["." for _ in range(width)])

        if etap == 3:
            break

        if val == "ENTER" and etap == 0:
            if (x, y) not in linie:
                linie.append((x, y))
            val = 0

        if val == "DEL" and etap == 0:
            if (x, y) in linie:
                del linie[linie.index((x, y))]
            val = 0


        if val == "ENTER" and etap == 1:
            if dodane[y][x] == ".":
                okno.append((x, y))
                dodane[y][x] = "+"
                val = 0

        if val == "DEL" and etap == 1:
            if dodane[y][x] == "+":
                del okno[okno.index((x, y))]
                dodane[y][x] = "."
                val = 0

        if val in range(1, 10) and etap == 2:
            liczby[y][x] = val
            val = 0

        if val == "DEL" and etap == 2:
            liczby[y][x] = "."
            val = 0

        if etap == 1:
            draw_dodane()

        draw()
        if etap == 0:
            draw_line()
        elif etap == 1:
            draw_box()
        elif etap == 2:
            draw_box()
            draw_liczby()
        pygame.display.update()
    pygame.quit()
