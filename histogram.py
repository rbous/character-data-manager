# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emma Tovell Baudier"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306794"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-028"

#==========================================#
# Place your histogram function after this line
import numpy as np
import matplotlib.pyplot as plt


def histogram(character_list: list[dict], attribute: str) -> float:
    """Return a histogram showing in a specified attribute how many of each category
    can be found in the dictionary. Will also return the maximum value, unless the 
    attribute has string values
    Preconditions: the inputs must be a list of dictionnaries and a string
    >>>histogram([{'Occupation': 'EB','Agility': 1}, {'Occupation': 'H', 'Agility': 11},
    {'Occupation': 'WA','Agility': 5}], "Occupation")
    -1
    >>>histogram([{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9,
     'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}], 'Personality')
    9
    >>>histogram([{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 20,
     'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}], 'Luck')
     0.72
    """
    if attribute == 'Occupation':
        x_value = []
        y_value = []
        for i in range(len(character_list)):
            if character_list[i]['Occupation'] not in x_value:
                x_value.append(character_list[i]['Occupation'])
                y_value.append(0)

        for i in range(len(character_list)):
            for j in range(len(x_value)):
                if character_list[i]['Occupation'] == x_value[j]:
                    y_value[j] += 1
        max_val = -1

    # if the input is for weapon
    elif attribute == 'Weapon':
        x_value = []
        y_value = []
        max_val = -1
        for i in range(len(character_list)):
            if character_list[i]['Weapon'] not in x_value:
                x_value.append(character_list[i]['Weapon'])
                y_value.append(0)
                #x_value[i] = str(x_value[i])

        # nested for loop to find how many weapons of each kind are in the character_list
        for i in range(len(character_list)):
            for j in range(len(x_value)):
                if character_list[i]['Weapon'] == x_value[j]:
                    y_value[j] += 1

    # any other values that are ints or floats
    else:
        # find the max value in the dict
        for i in range(len(character_list)):
            if i == 0:
                max_val = character_list[i][attribute]
            elif character_list[i][attribute] > max_val:
                max_val = character_list[i][attribute]
        # set the length of the list to 20
        x_value = [[0, 0]] * 20
        y_value = [0] * 20
        #print(attribute, 'maxval', max_val)
        x_range = max_val / 20
        new_val = 0
        # set the ranges of the histogram on the x value
        for i in range(len(x_value)):
            new_val += x_range
            x_value[i] = [x_range * i, new_val]

        # find how many attributes are in each bin
        for i in range(len(character_list)):
            for j in range(len(x_value)):
                if x_value[j][0] < character_list[i][attribute] <= x_value[j][1]:
                    y_value[j] += 1

        # change the x values in strings so that it can be processed by matplotlib
        for i in range(len(x_value)):
            #x_value[i] = float(x_value[i][0])
            x_value[i] = str(x_value[i][0]) + " to " + str(x_value[i][1])

    # create the histogram
    fig1 = plt.figure()

    plt.title(f"number of each {attribute} type")
    plt.xlabel('type of each indicated')
    plt.ylabel('number of each category')
    plt.bar(x_value, y_value, color='blue', width=0.4)
    plt.show()

    # return the max value of the list, unless the type is not an int and it will return -1
    return max_val

# Do NOT include a main script in your submission
