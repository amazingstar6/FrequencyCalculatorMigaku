def jlpt(file_words, file_jlpt, up_to_level):
    n5 = set()
    n4 = set()
    n3 = set()
    n2 = set()
    n1 = set()

    for i in file_jlpt['list']:
        for level in i[2]:
            word = i[0]
            if level == 'N5':
                n5.add(word)
            elif level == 'N4':
                n4.add(word)
            elif level == 'N3':
                n3.add(word)
            elif level == 'N2':
                n2.add(word)
            elif level == 'N1':
                n1.add(word)
    level_checker(file_words, n5, 'N5')
    if up_to_level < 5:
        level_checker(file_words, n4, 'N4')
    if up_to_level < 4:
        level_checker(file_words, n3, 'N3')
    if up_to_level < 3:
        level_checker(file_words, n2, 'N2')
    if up_to_level < 2:
        level_checker(file_words, n1, 'N1')


def level_checker(file_words, level_list, file="N"):
    count = 0
    known_words_list = set()
    for i in file_words:
        known_word = (i[0].split("◴"))[0]
        if known_word in level_list:
            count += 1
            known_words_list.add(known_word)
    unknowns = [x for x in level_list if x not in known_words_list]
    f = open(file + ".txt", 'w', encoding="UTF-8")
    for i in unknowns:
        f.write(i + "\n")
    print("Level " + file + " contains " + str(len(level_list)).ljust(4) + " words. ", end='')
    print(
        "You know " + str(round((((len(level_list) - len(unknowns)) / len(level_list)) * 100), 2)).ljust(5) +
        " % (" + str(len(known_words_list)).ljust(4) +
        " words) of those words.")
