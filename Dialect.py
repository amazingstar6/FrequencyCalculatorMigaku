def main(word_data, dialect_file, dialect_name):
    unknown_words_file = open("Dialect.txt", "w", encoding="UTF-8")
    known_words_list = []
    count = 0
    dictionary = {}
    for i in dialect_file['list']:
        if i[2][0] == dialect_name:
            dictionary[i[0]] = dialect_file['index'][i[2][0]]
    for i in word_data:
        word_data = (i[0].split("◴"))[0]
        if word_data in dictionary.keys():
            known_words_list.append(word_data)
            count += 1
    print(("%.2f" % (round((count / (len(dictionary)) * 100), 2))).ljust(5) + " % You know " + str(count).ljust(3) +
          " words from the " + (str(len(dictionary))).ljust(3) +
          " from the " + dialect_file['index'][dialect_name] + " dialect")
    unknown_words_list = (set(dictionary.keys()) - set(known_words_list))
    for i in unknown_words_list:
        unknown_words_file.write(i + "\n")


def dialect(word_data, dialect_file):
    dialects = []
    for i, j in dialect_file['index'].items():
        dialects.append(i)
    for i in dialects:
        main(word_data, dialect_file, i)
