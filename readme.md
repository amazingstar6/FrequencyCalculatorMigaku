# Setup
This python scripts asks for the name of you migaku known words file (when you export it as backup) and for the migaku Netflix frequency file which you can download from http://dicts.migaku.io/ja/frequency_lists/Netflix.json
<br><br>
Put the two .json files in the same directory as the .py file and run the .py file.<br><br>
If you have a weak computer, open the .py file in a text editor and delete the line 68 and 69:
``` 
print("For lower than 5 stars: ", end="")
frequencyCalculator((len(frequency) - 1), 60000)
```
Since it goes through almost the entire frequency list otherwise.
## Tutorial on running the python file
### Step 1: Opening the command prompt
One way to run the .py file is to open the command prompt in the directory where your files are, you can do this by clicking on the path in the file explorer and typing in "cmd" and then hitting enter.<br>
Another way is to open the command prompt by searching "cmd" in the search bar and typing the command "cd directory" where your replace "directory" with the directory your files are in.<br>
Otherwise just google it.<br>
### Step 2: Running the python file in the cmd
When the cmd is opened in the directory you can type "python frequencyCalculator.py"<br>
If you do not have Python installed, you can install it from here https://www.python.org/downloads/
