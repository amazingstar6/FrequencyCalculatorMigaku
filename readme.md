This python scripts calculates the percentage of words you know compared with the words in the specified frequency file.
# Setup
Download this repository (code -> Download ZIP) and export your Migaku Known Words file to the directory where you extracted this repository AND rename it to "Words.json".<br>
To run the script, run main.py
<br>
## Tutorial on running the python file
### Step 1: Opening the command prompt
One way to run the .py file is to open the command prompt in the directory where the repository is, you can do this by clicking on the path in the file explorer and typing in "cmd" and then hitting enter.<br>
Another way is to open the command prompt by typing "cmd" in the search bar and typing the command "cd directory" where your replace "directory" with the directory your files are in.<br>
Otherwise just google it.<br>
### Step 2: Running the python file in the cmd
When the cmd is opened in the directory you can type "python main.py"<br>
If you do not have Python installed, you can install it from here https://www.python.org/downloads/

# Inconsistencies
<i>I still need to improve the fact that the frequency files contains the kanji and the hiragana/katakana. It know only checks the kanji and for the frequency file visual novel for example it decreases the amount of words you know since they use kanji for words like する
.<br>It also still ignores the fact if a word is seen or know.<br>And because of inconsistencies like 二人 being parsed by Migaku as 二 and 人, those words won't be in your known word list and therefore also not seen as known when comparing them to the frequency list.</i>
