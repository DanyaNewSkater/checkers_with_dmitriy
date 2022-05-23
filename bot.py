import time, random

def moves_bot(position, color):
    '''Функция, ищущая возможные ходы для всех шашек одного цвета.'''
    matrixArea = [[[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], []]]
    taking = [[[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []],
              [[], [], [], [], [], [], [], []]]
    if color == "white":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 0:

                            matrixArea[i][j].append([i - 1, j - 1])

                        elif position[i - 1][j - 1] == 2 or position[i - 1][j - 1] == 22:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:

                                    taking[i][j].append([i - 2, j - 2])

                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 0:

                            matrixArea[i][j].append([i - 1, j + 1])

                        elif position[i - 1][j + 1] == 2 or position[i - 1][j + 1] == 22:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    taking[i][j].append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 2 or position[i + 1][j - 1] == 22:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:
                                    taking[i][j].append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 2 or position[i + 1][j + 1] == 22:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:
                                    taking[i][j].append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])


                elif position[i][j] == 11:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD,jD])
                            iD += 1
                            jD += 1
                            take = False
                            while iD != 8 and jD != 8 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0<=iD+1<= 7 and 0<=jD+1<= 7 and take == False and (position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD+=1
                                    jD+=1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD += 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD += 1
                            jD += 1
                            while iD != 8 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD -= 1
                            take = False
                            while iD != -1 and jD != -1 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD - 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD -= 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD -= 1
                            jD -= 1
                            while iD != -1 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD += 1
                            jD -= 1
                            take = False
                            while iD != 8 and jD != -1 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD + 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD += 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD += 1
                            jD -= 1
                            while iD != 8 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD += 1
                            take = False
                            while iD != -1 and jD != 8 and position[iD][jD] != 1 and position[iD][jD] != 11:
                                if 0 <= iD - 1 <= 7 and 0 <= jD + 1 <= 7 and take == False and (
                                        position[iD][jD] == 2 or position[iD][jD] == 22):
                                    iD -= 1
                                    jD += 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD += 1
                            break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            iD -= 1
                            jD += 1
                            while iD != -1 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            break


    if color == "black":
        for i in range(len(position)):
            for j in range(len(position[i])):
                if position[i][j] == 2:
                    if i + 1 < 8 and j - 1 >= 0:
                        if position[i + 1][j - 1] == 0:
                            matrixArea[i][j].append([i + 1, j - 1])

                        elif position[i + 1][j - 1] == 1 or position[i + 1][j - 1] == 11:
                            if i + 2 < 8 and j - 2 >= 0:
                                if position[i + 2][j - 2] == 0:

                                    taking[i][j].append([i + 2, j - 2])

                                    matrixArea[i][j].append([i + 2, j - 2])

                    if i + 1 < 8 and j + 1 < 8:
                        if position[i + 1][j + 1] == 0:

                            matrixArea[i][j].append([i + 1, j + 1])

                        elif position[i + 1][j + 1] == 1 or position[i + 1][j + 1] == 11:
                            if i + 2 < 8 and j + 2 < 8:
                                if position[i + 2][j + 2] == 0:

                                    taking[i][j].append([i + 2, j + 2])

                                    matrixArea[i][j].append([i + 2, j + 2])

                    # Проверка на возможность взятия назад
                    if i - 1 >= 0 and j - 1 >= 0:
                        if position[i - 1][j - 1] == 1 or position[i - 1][j - 1] == 11:
                            if i - 2 >= 0 and j - 2 >= 0:
                                if position[i - 2][j - 2] == 0:
                                    taking[i][j].append([i - 2, j - 2])
                                    matrixArea[i][j].append([i - 2, j - 2])

                    if i - 1 >= 0 and j + 1 < 8:
                        if position[i - 1][j + 1] == 1 or position[i - 1][j + 1] == 11:
                            if i - 2 >= 0 and j + 2 < 8:
                                if position[i - 2][j + 2] == 0:
                                    taking[i][j].append([i - 2, j + 2])

                                    matrixArea[i][j].append([i - 2, j + 2])



                elif position[i][j] == 22:
                    iD = i + 1
                    jD = j + 1
                    while iD != 8 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD,jD])
                            iD += 1
                            jD += 1
                            take = False
                            while iD != 8 and jD != 8 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0<=iD+1<= 7 and 0<=jD+1<= 7 and take == False and (position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD+=1
                                    jD+=1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD += 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD += 1
                            jD += 1
                            while iD != 8 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break

                    iD = i - 1
                    jD = j - 1
                    while iD != -1 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD -= 1
                            take = False
                            while iD != -1 and jD != -1 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD - 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD -= 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD -= 1
                            jD -= 1
                            while iD != -1 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break


                    iD = i + 1
                    jD = j - 1
                    while iD != 8 and jD != -1:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD += 1
                            jD -= 1
                            take = False
                            while iD != 8 and jD != -1 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD + 1 <= 7 and 0 <= jD - 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD += 1
                                    jD -= 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD += 1
                                jD -= 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD += 1
                            jD -= 1
                            while iD != 8 and jD != -1 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD += 1
                                jD -= 1
                            else:
                                break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break

                    iD = i - 1
                    jD = j + 1
                    while iD != -1 and jD != 8:
                        if position[iD][jD] == 0:
                            matrixArea[i][j].append([iD, jD])
                            iD -= 1
                            jD += 1
                            take = False
                            while iD != -1 and jD != 8 and position[iD][jD] != 2 and position[iD][jD] != 22:
                                if 0 <= iD - 1 <= 7 and 0 <= jD + 1 <= 7 and take == False and (
                                        position[iD][jD] == 1 or position[iD][jD] == 11):
                                    iD -= 1
                                    jD += 1
                                    take = True
                                    if position[iD][jD] == 0:
                                        matrixArea[i][j].append([iD, jD])
                                        taking[i][j].append([iD, jD])
                                    else:
                                        break
                                elif position[iD][jD] == 0:
                                    if take:
                                        taking[i][j].append([iD, jD])
                                    matrixArea[i][j].append([iD, jD])
                                else:
                                    break
                                iD -= 1
                                jD += 1
                            break

                        elif position[iD][jD] == 1 or position[iD][jD] == 11:
                            iD -= 1
                            jD += 1
                            while iD != -1 and jD != 8 and position[iD][jD] == 0:
                                taking[i][j].append([iD, jD])
                                matrixArea[i][j].append([iD, jD])
                                iD -= 1
                                jD += 1
                            else:
                                break

                        elif position[iD][jD] == 2 or position[iD][jD] == 22:
                            break
    return [matrixArea, taking]


def move_bot(fr, to, area):
    '''Функция, делающая ход бота.'''
    if area[fr[0]][fr[1]] == 11 or area[fr[0]][fr[1]] == 22:
        shape = area[fr[0]][fr[1]]
        iFr = fr[0]
        jFr = fr[1]
        iTo = to[0]
        jTo = to[1]
        area[iTo][jTo] = shape
        area[iFr][jFr] = 0

    else:
        if abs(fr[0] - to[0]) == 1 and abs(fr[1] - to[1]) == 1:
            shape = area[fr[0]][fr[1]]
            if shape == 1 and to[0] == 0:
                shape = 11
            elif shape == 2 and to[0] == 7:
                shape = 22
            iFr = fr[0]
            jFr = fr[1]
            iTo = to[0]
            jTo = to[1]
            area[iTo][jTo] = shape
            area[iFr][jFr] = 0

        elif abs(fr[0] - to[0]) == 2 and abs(fr[1] - to[1]) == 2:
            shape = area[fr[0]][fr[1]]
            if shape == 1 and to[0] == 0:
                shape = 11
            elif shape == 2 and to[0] == 7:
                shape = 22
            iFr = fr[0]
            jFr = fr[1]
            iTo = to[0]
            jTo = to[1]
            area[iTo][jTo] = shape
            area[iFr][jFr] = 0
            area[abs((iTo + iFr)) // 2][abs((jTo + jFr)) // 2] = 0

    return True

def bot_level_1(area):
    '''Функция бота 1 уровня, делающего обязательные взятия и рандомные ходы.'''
    forLevel1 = []
    ask = take_go(area)
    # print(ask)

    if ask == "No":
        matrixArea = moves_bot(area, "black")[0]
        for i in range(len(matrixArea)):
            for j in range(len(matrixArea[i])):
                if matrixArea[i][j] != [] and area[i][j] == 2 or area[i][j] == 22:
                    forLevel1.append([[i, j], matrixArea[i][j]])
            # print(matrixArea[i])
        if forLevel1 == []:
            for i in range(len(area)):
                for j in range(len(area[i])):
                    if area[i][j] == 2 or area[i][j] == 22:
                        area[i][j] = 0
        else:
            hod = random.choice(forLevel1)
            fr1 = hod[0]
            to1 = random.choice(hod[1])
            move_bot(fr1, to1, area)

def take_go(area, iT = "Null", jT = "Null"):
    '''Функция для обязательного взятия.'''
    isBreak = False
    matrixArea = moves_bot(area, "black")[0]
    taking = moves_bot(area, "black")[1]
    count = 0
    isStop = True
    if iT != "Null":
        if taking[iT][jT] != []:
            take = taking[iT][jT][0]
            iTo = take[0]
            jTo = take[1]
            shape = area[iT][jT]
            if shape == 1 and iTo == 0:
                shape = 11
            elif shape == 2 and iTo == 7:
                shape = 22
            area[iTo][jTo] = shape
            area[iT][jT] = 0
            area[abs((iTo + iT)) // 2][abs((jTo + jT)) // 2] = 0
            isStop = False
            count += 1
            iT = iTo
            jT = jTo
    else:
        for i in range(len(taking)):
            for j in range(len(taking[i])):
                # print(taking[i][j])
                if taking[i][j] != [] and (area[i][j] == 1 or area[i][j] == 2):
                    take = taking[i][j][0]
                    iTo = take[0]
                    jTo = take[1]
                    shape = area[i][j]
                    if iTo == 0:
                        shape = 11
                    elif iTo == 7:
                        shape = 22
                    area[iTo][jTo] = shape
                    area[i][j] = 0
                    area[abs((iTo + i)) // 2][abs((jTo + j)) // 2] = 0
                    isStop = False
                    count += 1
                    iT = iTo
                    jT = jTo
                    isBreak = True
                    break

                if taking[i][j] != [] and (area[i][j] == 11 or area[i][j] == 22):
                    print("Хочу взять")
                    count += 1
                    isStop = False
                    take = taking[i][j][0]
                    iTo = take[0]
                    jTo = take[1]
                    shape = area[i][j]
                    area[iTo][jTo] = shape
                    area[i][j] = 0
                    countI = i
                    countJ = j
                    while countI != iTo and countJ != jTo:

                        if (area[countI][countJ] == 11 or area[countI][countJ] == 1) and shape == 22:
                            area[countI][countJ] = 0
                            break
                        elif (area[countI][countJ] == 22 or area[countI][countJ] == 2) and shape == 11:
                            area[countI][countJ] = 0
                            break
                        if countI < iTo:
                            countI += 1
                        elif countI > iTo:
                            countI -= 1
                        if countJ < jTo:
                            countJ += 1
                        elif countJ > jTo:
                            countJ -= 1
                    isBreak = True
                    break
            if isBreak:
                break
    if isStop and count == 0:
        # Взятий не было
        return "No"
    elif isStop and count != 0:
        # Взятия были
        return "Yes"
    elif not isStop and count != 0:
        # Пытаемся продолжить брать
        take_go(area, iT, jT)

def mark(position, color):
    '''Функция оценки положения шашек.'''
    winWhite = False
    winBlack = False
    for i in range(len(position)):
        if position[i].count(1) != 0 or position[i].count(11) != 0:
            winWhite = True
        if position[i].count(2) != 0 or position[i].count(22) != 0:
            winBlack = True
    if winWhite and not winBlack and color == "white":
        return "Белые победили"
    elif not winWhite and winBlack and color == "white":
        return "Чёрные победили"
    elif winWhite and not winBlack and color == "black":
        return "Чёрные победили"
    elif not winWhite and winBlack and color == "black":
        return "Белые победили"
    return "Null"