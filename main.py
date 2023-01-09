import codecs
import json
from Netflix import netflix
from JLPT import jlpt

frequencyFileNumber = int(input("""
After execution, there will be a text file generated with the corresponding name of the frequency file(s) with all the words that weren't in your known words list.

Which frequency file would you like to use to compare with your known words?
1. Narou (Not yet implemented)
2. Netflix
3. Novel 5k (Not yet implemented)
4. Slife of Life (Not yet implemented)
5. Shonen (Not yet implemented)
6. Visual Novel (Not yet implemented)
7. JLPT
8. Wanikani (Not yet implemented)
9. Dialect (Not yet implemented)
"""))

if frequencyFileNumber < 7:
    stars = int(input("Up to how many stars do you want to analyze? "))
elif frequencyFileNumber == 7:
    level = int(input("Up to which level do you want to analyze? (e.g. \"3\") "))

# fileNameFrequency = input("What is the file name of the frequency list? (e.g. \"Netflix.json\") ")
if frequencyFileNumber == 2:
    fileNameFrequency = "Netflix.json"
elif frequencyFileNumber == 7:
    fileNameFrequency = "JLPT.json"

# fileNameWords = input("What is the file name of your Migaku Known Words list? (e.g. \"Words.json\") ")
fileNameWords = "Words.json"

dataFrequency = json.load(codecs.open(fileNameFrequency, 'r', 'utf-8-sig'))

with open(fileNameWords, 'r', encoding='UTF-8') as file:
    dataWords = json.load(file)

if frequencyFileNumber == 2:
    netflix(dataWords, dataFrequency, stars)
if frequencyFileNumber == 7:
    jlpt(dataWords, dataFrequency, level)