# **Character data management**
This project is a character data management software. It uses a file with a character and its attributes listed on each line and can perform the following commands: load the data, sort it in ascending or descending order using a particular attribute, find a polynomial equation that best fits the “Health” attribute when compared to another attribute, and plot the histogram of the values of an attribute.

## Date
07/04/2024

## Software name and version
Python 3.11

## Contact information
Rayane Boussanni - rayaneboussanni@cmail.carleton.ca

## Dependencies
You will need to have the following downloaded for the software to run:
-	Python 3.11
-	Any python IDE / shell
-	matplotlib.pyplot version 3.8.4
-	numpy version 1.26.0
-	check.py module

## Installation
After installing python and all other dependencies, unzip the folder, and save all files in the same location. Then, run ‘text.UI’ in the IDE of your choice, and it will prompt you to enter your command. The file with your data must be in the same location as the rest of the files. If you already have a command file outlined with your desired actions, run ‘batch.UI’ instead. The file with the commands must also be in the same location as the rest of the files.

## Usage

### Text User Interface
To use text_UI.py, simply run the script and follow the prompts displayed on the screen. Enter either uppercase or lowercase letters to execute commands, such as "L" for loading data, "S" for sorting data, "C" for curve fitting, "H" for histogram, or "E" to exit the program.

### Batch User Interface
To use batch_UI.py, first, create a text file containing one complete command per line, with each command's inputs separated by semicolons. Then, execute the batch_UI.py script. When prompted, input the name of the text file containing the commands. The script will process each command from the file, displaying output in the terminal as required. Commands in the text file should adhere to the same format as those in the text-based UI.

## Credits

### Rayane:
-	character_strength_list function
-	calculate_health function
-	test_calculate_health function (test 4)
-	sort_characters_intelligence_selection function
-	sort function
-	curve_fit function

### Emma:
-	character_occupation_list function
-	load_data function
-	test_return_list_correct_length function (test 2)
-	sort_characters_agility_bubble function
-	histogram function

### Aya:
-	character_luck_list function
-	test_return_correct_dict_inside_list function (test 3)
-	load_data module
-	sort_characters_armor_bubble function
-	text user interface

### Jack:
-	character_weapon_list function
-	test_return_list function (test 1)
-	test_load_data module
-	sort_characters_health_insertion function
-	batch user interface

## License
MIT License

Copyright © 2024 [Rayane Boussanni]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
