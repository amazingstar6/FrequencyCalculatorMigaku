from ConvertListtoDic import convert


def netflix(file_words, file_frequency, stars=6):
    main(file_words, file_frequency, 1)
    if stars > 1:
        main(file_words, file_frequency, 2)
    if stars > 2:
        main(file_words, file_frequency, 3)
    if stars > 3:
        main(file_words, file_frequency, 4)
    if stars > 4:
        main(file_words, file_frequency, 5)
    if stars > 5:
        main(file_words, file_frequency, 6)


def main(file_words, file_frequency, stars):
    frequency_list = []
    for i in file_frequency:
        frequency_list.append(i[0])
    begin = 0
    end = 0
    if stars < 1 or stars > 6:
        raise Exception("Choose stars between 1 and 6")
    if stars == 1:
        begin = 0
        end = 1500
    elif stars == 2:
        begin = 1500
        end = 5000
    elif stars == 3:
        begin = 5000
        end = 15000
    elif stars == 4:
        begin = 15000
        end = 30000
    elif stars == 5:
        begin = 30000
        end = 60000
    elif stars == 6:
        begin = 60000
        end = len(frequency_list) - 1
    known_words_list = []
    count = 0
    convert(file_frequency)
    for i in file_words:
        word_data = (i[0].split("◴"))[0]
        if word_data in frequency_list[begin:end]:
            known_words_list.append(word_data)
            count += 1
    print((str(round((count / (end - begin) * 100), 2))).ljust(5) + " %. You know " + str(
        count) + " words from the most common " + str(begin) + "-" + str(end))
    # writes to the file unknownWords.html all the words you are in the frequency area that you do NOT know
    unknown_words_file = open("Netflix.txt", "w", encoding="UTF-8")
    list_frequency = frequency_list[begin:end]
    unknown_words_list = (set(list_frequency) - set(known_words_list))
    for i in unknown_words_list:
        unknown_words_file.write(i + "\n")
