# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rayane Boussanni"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101319770"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your curve_fit function after this line

import numpy as np


def curve_fit(characters: list[dict], attribute: str, deg: int) -> str:
    """Returns a string representation of the equation of the best fit for the average of health given the list of
    characters, the attribute it is compared to, and the degree of the polynomial desired.
    Precondition: 1 <= degree <= 5
    >>> curve_fit([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Health': 115.0}, {'Occupation': 'EB', 'Strength': 9, 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8, 'Health': 68.0}, {'Occupation': 'H', 'Strength': 13, 'Agility': 6, 'Stamina': 5, 'Personality': 6, 'Intelligence': 13, 'Luck': 0.67, 'Armor': 9, 'Health': 97.27000000000001}, {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Health': 83.0}], 'Stamina', 1)
    'y = -5.716666666666666x+126.54666666666668'
    >>> curve_fit([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Health': 115.0}, {'Occupation': 'EB', 'Strength': 9, 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8, 'Health': 68.0}, {'Occupation': 'H', 'Strength': 13, 'Agility': 6, 'Stamina': 5, 'Personality': 6, 'Intelligence': 13, 'Luck': 0.67, 'Armor': 9, 'Health': 97.27000000000001}, {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Health': 83.0}], 'Stamina', 2)
    'y = -0.08488188976377936x^2+-4.703280839895008x+124.30855643044612'
    >>> curve_fit([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Health': 115.0}, {'Occupation': 'EB', 'Strength': 9, 'Agility': 3, 'Stamina': 10, 'Personality': 8, 'Intelligence': 6, 'Luck': 0.5, 'Armor': 8, 'Health': 68.0}, {'Occupation': 'H', 'Strength': 13, 'Agility': 6, 'Stamina': 5, 'Personality': 6, 'Intelligence': 13, 'Luck': 0.67, 'Armor': 9, 'Health': 97.27000000000001}, {'Occupation': 'WA', 'Strength': 14, 'Agility': 7, 'Stamina': 8, 'Personality': 8, 'Intelligence': 7, 'Luck': 0.39, 'Armor': 10, 'Health': 83.0}], 'Stamina', 5)
    'y = -0.09261111111111081x^3+1.5813888888888792x^2+-13.367888888888855x+136.1511111111112'
    """
    attr_levels = {char[attribute] for char in characters}  # get all point values for the attribute
    x, y = [], []  # initialize x and y

    # getting x and y
    for level in attr_levels:  # iterate through all attribute point values
        y.append(level)  # add level to y
        cur_health = []  # initialize list that will contain the health values associated with the current level
        for char in characters:
            if char[attribute] == level:  # verify if the attribute level is the current point value
                cur_health.append(char['Health'])
        x.append(sum(cur_health)/len(cur_health))  # calculate and add the health average to x

    # writing out the equation
    degree = deg if deg <= len(attr_levels) - 1 else len(attr_levels) - 1  # choose to do interpolation or regression
    coefs = np.polyfit(y, x, degree)[::-1]  # calculate coefficients
    equation = f"{coefs[1]}x+{coefs[0]}"  # write the first two terms
    for i in range(2, len(coefs)):
        equation = str(coefs[i]) + "x^" + str(i) + "+" + equation  # add all terms that are degree 2 or more
    return "y = " + equation


# Do NOT include a main script in your submission
