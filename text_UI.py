# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Aya Skinner"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297604"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-028"


#==========================================#
# Place your script for your text_UI after this line
from load_data import *
from sort import *
from curve_fit import *
from histogram import *

try:
    while True:
        print("""The available commands are:\n    L)oad Data\n    S)ort Data\n    C)urve fit
    H)istrogram\n    E)xit\n""")
        command = input("Please type your command: ").upper()
        if command == "L":
            try:
                filename = input("Please enter the name of the file: ")
                file = open(filename)
                file.close()
                while True:
                    command = input("Please enter the attribute to use as a filter: ").capitalize()
                    if command == "Strength" or command == "Luck" or command == "Occupation" or command == "Weapon" or command == "All":
                        if command == "All":
                            key = 0
                        else:
                            while True:
                                try:
                                    key = input("Please enter the value of the attribute: ")
                                    if command == "Strength":
                                        key = tuple(map(int, key.strip("() ").split(',')))
                                        if len(key) != 2 or type(key[0]) != int or type(key[1]) != int:
                                            raise ValueError
                                    elif command == "Occupation" or command == "Weapon": pass
                                    else: key = float(key)
                                    break
                                except ValueError:
                                    print("Invalid value")
                                    continue
                        data = load_data(filename, (command, key))
                        if (command == "Strength" or command == "Luck") and data != []:
                            for i in range(len(data)):
                                data[i].update({command: 0})
                            data = calculate_health(data)
                            for i in range(len(data)):
                                data[i].pop(command)
                        elif data != []:
                            data = calculate_health(data)
                        print("data loaded")
                        break
                    else:
                        print("The attribute is invalid")
            except OSError:
                print("The file does not exist or could not be loaded.")
        elif command == "S":
            try:
                if data == 0:
                    pass
            except:
                print("File not loaded. Please load a file first")
                continue
            while True:
                command = input("""Please enter the attribute you want to use for sorting:
'Agility', 'Armor', 'Intelligence', 'Health'\n: """).capitalize()
                if command == 'Agility' or command == 'Armor' or command == 'Intelligence' or command == 'Health':
                    break
                else:
                    print("Invalid attribute")
            while True:
                order = input("Ascending (A) or Descending (D) order: ").upper()
                if order == "A" or order == "D":
                    break
                else: print("Invalid ordering")
            sort(data, order, command)
            while True:
                command = input("Data sorted. Do you want to display the data? (Y/N): ").upper()
                if command == "Y":
                    print(data)
                    break
                elif command == "N":
                    break
        elif command == "C":
            try:
                if data == 0:
                    pass
            except:
                print("File not loaded. Please load a file first")
                continue
            print("Please enter the attribute you want to find the best fit for")
            num = 0
            for i in data[0].keys():
                num = num + 1
                if type(data[0][i]) == int or type(data[0][i]) == float:
                    print(f"'{i}'", end = "")
                    if num != len(data[0].keys()):
                        print(", ", end = "")                        
            command = input("\n: ").capitalize()
            if not command in data[0].keys():
                print("Invalid command")
                continue
            try:
                number = int(input("Please enter the order of the polynomial to be fitted (1 to 5): "))
            except TypeError:
                print("Invalid number")
                continue
            if number >= 1 and number <= 5:
                print(curve_fit(data, command, number))
            else: 
                print("Number out of range")
        elif command == "H":
            try:
                if data == 0:
                    pass
            except:
                print("File not loaded. Please load a file first")
                continue         
            print("Please enter the attribute you want to use for plotting")
            num = 0
            for i in data[0].keys():
                num = num + 1
                if type(data[0][i]) == int or type(data[0][i]) == float:
                    print(f"'{i}'", end = "")
                    if num != len(data[0].keys()):
                        print(", ", end = "")                        
            command = input("\n: ").capitalize()
            if not command in data[0].keys():
                print("Invalid command")
                continue
            histogram(data, command)
        elif command == "E":
            break
        else:
            print("Invalid command")
except EOFError:
    pass