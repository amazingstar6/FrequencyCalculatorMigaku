import codecs
import json
from Netflix import netflix
from JLPT import jlpt
from WaniKani import wanikani
from Dialect import dialect

frequencyFileNumber = int(input("""
After execution, there will be a text file generated with the corresponding name of the frequency file(s)
with all the words that weren't in your known words list.

Which frequency file would you like to use to compare with your known words?
1. Narou
2. Netflix
3. Novel 5k
4. Slice of Life
5. Shonen
6. Visual Novel
7. JLPT
8. Wanikani
9. Dialect
"""))

stars = 0
level = 0
if frequencyFileNumber < 7:
    stars = int(input("Up to how many stars do you want to analyze? (e.g. \"4\") "))
elif frequencyFileNumber == 7 or frequencyFileNumber == 8:
    level = int(input("Up to which level do you want to analyze? (e.g. \"3\") "))
elif frequencyFileNumber == 9:
    pass
else:
    raise Exception("Choose a better number for the stars or levels!")

if frequencyFileNumber == 1:
    fileNameFrequency = "Narou.json"
elif frequencyFileNumber == 2:
    fileNameFrequency = "Netflix.json"
elif frequencyFileNumber == 3:
    fileNameFrequency = "Novel 5k.json"
elif frequencyFileNumber == 4:
    fileNameFrequency = "Slice of Life.json"
elif frequencyFileNumber == 5:
    fileNameFrequency = "Shonen.json"
elif frequencyFileNumber == 6:
    fileNameFrequency = "Visual Novel.json"
elif frequencyFileNumber == 7:
    fileNameFrequency = "JLPT.json"
elif frequencyFileNumber == 8:
    fileNameFrequency = "Wanikani.json"
elif frequencyFileNumber == 9:
    fileNameFrequency = "Dialect.json"
else:
    raise Exception("Choose an actual number that is displayed in the help menu!")

fileNameWords = "Words.json"

dataFrequency = json.load(codecs.open(fileNameFrequency, 'r', 'utf-8-sig'))

with open(fileNameWords, 'r', encoding='UTF-8') as file:
    dataWords = json.load(file)

if frequencyFileNumber < 7:
    netflix(dataWords, dataFrequency, stars)
if frequencyFileNumber == 7:
    jlpt(dataWords, dataFrequency, level)
if frequencyFileNumber == 8:
    wanikani(dataWords, dataFrequency, level)
if frequencyFileNumber == 9:
    dialect(dataWords, dataFrequency)
