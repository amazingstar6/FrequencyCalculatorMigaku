import json

# index 0 = word
# index 1 = either 1 for seen or 2 for known
filename = input("What is the file name of your known word list? (e.g. words.json) ")
f = open(filename, encoding="UTF-8")
data = json.load(f)

# index 0 = word
# index 1 = "freq"
# index 2 = frequency number
# Download the frequency file from https://dicts.migaku.io/ja/frequency.json
frequencyFileName = input("What is the file name of the Netflix frequency file? (e.g. frequency.json) ")
fr = open(frequencyFileName, encoding="UTF-8")
frequency = json.load(fr)

# creating list of the words of the frequency json only
listFrequencyWords = []
for i in frequency:
    listFrequencyWords.append(i[0])


def frequencyCalculator(frequency: int, begin = 0):
    knownWordsList = []
    count = 0   
    for i in data:
        wordData = (i[0].split("◴"))[0]
        if wordData in listFrequencyWords[begin:frequency]:
            knownWordsList.append(wordData)
            count += 1
    print(str(round((count/(frequency-begin) * 100), 2)) + " %. You know " + str(count) + " words from the most common " + str(begin) + "-" + str(frequency))
    """
    # writes to the file unknownWords.html all the words you are in the frequency area that you do NOT know
    unknownWordsFile = open("unknownWords.html", "w", encoding="UTF-8")
    listfreq = listFrequencyWords[:frequency]
    unknownWordsList = list(set(listfreq) - set(knownWordsList))
    for i in unknownWordsList:
        unknownWordsFile.write(i + "\n")
    """

def searchFrequencyFile(word):
    for i in frequency:
        if word == i[0]:
            print(i[0] + " has a frequency of: " + " " + str(frequency.index(i)))

def searchKnownWordsFile(word):
    for i in data:
        if word == (i[0].split("◴"))[0]:
            print("You know this word: " + (i[0].split("◴"))[0])

def searchBothFiles(word):
    searchFrequencyFile(word)
    searchKnownWordsFile(word)

def caluclateForEveryStar():
    print("For 1 star: ", end="")
    frequencyCalculator(1500)
    print("For 2 stars: ", end="")
    frequencyCalculator(5000, 1500)
    print("For 3 stars: ", end="")
    frequencyCalculator(15000, 5000)
    print("For 4 stars: ", end="")
    frequencyCalculator(30000, 15000)
    print("For 5 stars: ", end="")
    frequencyCalculator(60000, 30000)
    print("For lower than 5 stars: ", end="")
    frequencyCalculator((len(frequency) - 1), 60000)

caluclateForEveryStar()

# searchBothFiles("犯罪")


# for i in data:
#     wordData = (i[0].split("◴"))[0]
#     if wordData in listFrequencyWords

# for i in data:
#     print(i[0].split("◴")[0])
# print(type(data))
# print(frequency[0][0])
# print(((data[0][0]).split("◴"))[0])
f.close
fr.close