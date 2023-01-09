import json
from ConvertListtoDic import Convert


with open('Wanikani.json', encoding='UTF-8') as file:
    data = json.load(file)
print(data['list'][55])

with open('Words.json', encoding='UTF-8') as file:
    dataWords = json.load(file)

unknownWordsFile = open("WaniKani.txt", "w", encoding="UTF-8")

def main(dataword, wanikaniFile, level):
    knownWordsList = []
    count = 0
    wanikaniList = []
    levellist = []
    for i in wanikaniFile['list']:
        wanikaniList.append(i[0])
        if i[2][0] == ('WK' + str(level)):
            levellist.append(i[0])
    for i in dataword:
        wordData = (i[0].split("◴"))[0]
        if wordData in levellist:
            knownWordsList.append(wordData)
            count += 1
    print(("%.2f" % (round((count/(len(levellist)) * 100), 2))).ljust(5) + " % You know " + str(count).ljust(3) + " words from the " + (str(len(levellist))).ljust(4) + "from level " + str(level))
    # writes to the file unknownWords.html all the words you are in the frequency area that you do NOT know
    unknownWordsList = (set(levellist) - set(knownWordsList))
    unknownWordsFile.write("Level " + str(level) + "\n")
    for i in unknownWordsList:
        unknownWordsFile.write(i + "\n")

def Wanikani(dataword, wanikaniFile, level):
    x = range(1, level + 1)
    for i in x:
        main(dataWords, data, i)