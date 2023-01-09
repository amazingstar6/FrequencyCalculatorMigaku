unknownWordsFile = open("WaniKani.txt", "w", encoding="UTF-8")


def main(data_word, wanikani_file, level):
    known_words_list = []
    count = 0
    wanikani_list = []
    level_list = []
    for i in wanikani_file['list']:
        wanikani_list.append(i[0])
        if i[2][0] == ('WK' + str(level)):
            level_list.append(i[0])
    for i in data_word:
        word_data = (i[0].split("◴"))[0]
        if word_data in level_list:
            known_words_list.append(word_data)
            count += 1
    print(("%.2f" % (round((count / (len(level_list)) * 100), 2))).ljust(5) + " % You know " + str(count).ljust(
        3) + " words from the " + (str(len(level_list))).ljust(4) + "from level " + str(level))
    # writes to the file unknownWords.html all the words you are in the frequency area that you do NOT know
    unknown_words_list = (set(level_list) - set(known_words_list))
    unknownWordsFile.write("Level " + str(level) + "\n")
    for i in unknown_words_list:
        unknownWordsFile.write(i + "\n")


def wanikani(data_word, wanikani_file, level):
    x = range(1, level + 1)
    for i in x:
        main(data_word, wanikani_file, i)
