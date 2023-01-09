def jlpt(fileWords, fileJlpt, upToLevel):
    n5 = []
    n4 = []
    n3 = []
    n2 = []
    n1 = []

    for i in fileJlpt['list']:
        level = i[2][0]
        word = i[0]
        if level == 'N5':
            n5.append(word)
        elif i[2][0] == 'N4':
            n4.append(word)
        elif level == 'N3':
            n3.append(word)
        elif level == 'N2':
            n2.append(word)
        elif level == 'N1':
            n1.append(word)
        if len(i[2]) >= 2:
            level = i[2][1]
            if level == 'N5':
                n5.append(word)
            elif i[2][0] == 'N4':
                n4.append(word)
            elif level == 'N3':
                n3.append(word)
            elif level == 'N2':
                n2.append(word)
            elif level == 'N1':
                n1.append(word)
    levelChecker(fileWords, n5, 'N5')
    if upToLevel < 5:
        levelChecker(fileWords, n4, 'N4')
    if upToLevel < 4:
        levelChecker(fileWords, n3, 'N3')
    if upToLevel < 3:
        levelChecker(fileWords, n2, 'N2')
    if upToLevel < 2:
        levelChecker(fileWords, n1, 'N1')

def levelChecker(fileWords, levelList, file="N"):
    count = 0
    knownWordsList = []
    for i in fileWords:
        knownWord = (i[0].split("◴"))[0]
        if knownWord in levelList:
            count += 1
            knownWordsList.append(knownWord)
    unknowns = [x for x in levelList if x not in knownWordsList]
    f = open(file + ".txt", 'w', encoding="UTF-8")
    for i in unknowns:
        f.write(i + "\n")
    print("Level " + file + " contains " + str(len(levelList)) + " words. ", end='')
    print("You know " + str(round((((len(levelList) - len(unknowns)) / len(levelList)) * 100), 2)) + " % of those words.")