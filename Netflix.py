import codecs
import json
from ConvertListtoDic import Convert

def netflix(fileWords, fileFrequency, stars = 6):
    main(fileWords, fileFrequency, 1)
    if stars > 1:
        main(fileWords, fileFrequency, 2)
    if stars > 2:
        main(fileWords, fileFrequency, 3)
    if stars > 3:
        main(fileWords, fileFrequency, 4)
    if stars > 4:
        main(fileWords, fileFrequency, 5)
    if stars > 5:
        main(fileWords, fileFrequency, 6)

def main(fileWords, fileFrequency, stars):
    frequencyList = []
    for i in fileFrequency:
        frequencyList.append(i[0])
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
        end = len(frequencyList) - 1
    knownWordsList = []
    count = 0
    dictionaryNetflix = Convert(fileFrequency)   
    for i in fileWords:
        wordData = (i[0].split("◴"))[0]
        if wordData in frequencyList[begin:end]:
            knownWordsList.append(wordData)
            count += 1
    print(str(round((count/(end-begin) * 100), 2)) + " %. You know " + str(count) + " words from the most common " + str(begin) + "-" + str(end))
    # writes to the file unknownWords.html all the words you are in the frequency area that you do NOT know
    unknownWordsFile = open("Netflix.txt", "w", encoding="UTF-8")
    listfreq = frequencyList[begin:end]
    unknownWordsList = (set(listfreq) - set(knownWordsList))
    for i in unknownWordsList:
        unknownWordsFile.write(i + "\n")

