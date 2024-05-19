# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Aya Skinner, Rayane Boussanni, Jack Tremblay-Lessard, Emma Tovell Baudier"

# Update "" with your team (e.g. T102)
__team__ = "T-28"


#==========================================#
# Place your sort_characters_agility_bubble function after this line

def sort_characters_agility_bubble(characters_list: list[dict], sort_order: str) -> list[dict]:
    """Returns a list of dictionaries sorted in either ascending or descending order of Agility,
    unless Agility isn't present in the list in which case the original list is returned
    Preconditions: the input values must be a list of dictionaries and a string

    >>>sort_characters_agility_bubble([{'Occupation': 'EB',
    'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility':13}]
    >>>sort_characters_agility_bubble([{'Occupation':'EB'},{'Occupation': 'M'}], "A")
    "Agility" key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]
    >>>sort_characters_agility_bubble([{'Occupation': 'EB','Agility': 1}, {'Occupation': 'H', 'Agility': 11},
    {'Occupation': 'EB','Agility': 5}], "D")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 5}, {'Occupation': 'EB', 'Agility': 1}]
    """
    sort = False
    # check to see if Agility is in the dictionary
    for i in range(len(characters_list) - 1):
        if 'Agility' in characters_list[i]:
            sort = True
    # if the key is in the dictionary
    if sort:
       # ascending bubble sort
        if sort_order == 'A':
            change = True
            # will iterate through the for loop as long as elements are being swapped
            while change:
                change = False
                for i in range(len(characters_list) - 1):
                    # if the element on the left is larger than the element on the right, swap them
                    if characters_list[i]['Agility'] > characters_list[i + 1]['Agility']:
                        characters_list[i], characters_list[i +
                                                            1] = characters_list[i + 1], characters_list[i]
                        swap = True
        # descending bubble sort
        elif sort_order == 'D':
            change = True
            # continue iterating through the for loop while there are elements being swapped
            while change:
                change = False
                for i in range(len(characters_list) - 1):
                    # if the element to the left is smaller than the element to the right, swap them
                    if characters_list[i]['Agility'] < characters_list[i + 1]['Agility']:
                        characters_list[i], characters_list[i +
                                                            1] = characters_list[i + 1], characters_list[i]
                        change = True
    # If the key is not in the dictionary
    else:
        print("\"Agility\" key is not present")

    # return the original list, either sorted or unsorted
    return characters_list


#==========================================#
# Place your sort_characters_intelligence_selection function after this line

def sort_characters_intelligence_selection(lst: list[dict], order: str) -> list[dict]:
    """returns a sorted list of characters' dictionaries by the "Intelligence" attribute using selection sort, given the inputted list and a string of either A or D indicating if it will be sorted in ascending or descending order.
    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 9}, {'Occupation': 'H', 'Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB', 'Intelligence': 9}]
    >>> sort_characters_intelligence_selection([{'Occupation':'EB'}, {'Occupation': 'M'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    """
    try:
        # selection sort algorithm
        for i in range(len(lst)):                                               # iterate through the entire list
            min_index = i                                                       # initialize current minimal value
            for j in range(i+1, len(lst)):                                      # iterate through the rest of the list

                if order == 'A':                                                    # if order increasing
                    if lst[min_index]["Intelligence"] > lst[j]["Intelligence"]:     # check if the current value is smaller than the current minimum
                        min_index = j                                               # if so, assign it

                elif order == 'D':                                                  # if order decreasing
                    if lst[min_index]["Intelligence"] < lst[j]["Intelligence"]:     # check if the current value is bigger than the current minimum
                        min_index = j                                               # if so, assign it

            lst[min_index], lst[i] = lst[i], lst[min_index]                     # swap current index and smallest value

    except KeyError:                                                            # if intelligence is not a key
        print('"Intelligence" key is not present')

    finally:
        return lst


#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(dict_list: list[dict], order: str) -> list[dict]:
    """Return a list of the characters sorted in either ascending or descending order according to their health.

    Preconditions: order == "A" or order == "D"

    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A")
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]

    >>> sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    "Health" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    >>> sort_characters_health_insertion([{'Weapon': 'Club', 'Health': 12}, {'Weapon': 'Staff', 'Health': 23}, {'Weapon': 'Club', 'Health': 16}], "D")
    [{'Weapon': 'Staff', 'Health': 23}, {'Weapon': 'Club', 'Health': 16}, {'Weapon': 'Club', 'Health': 12}]
    """

    if len(dict_list) > 0:
        if "Health" in dict_list[0]:
            # Order ascending
            if order == "A":
                # Traverse 1 through len(dict_list)
                for i in range(1, len(dict_list)):
                    key_dict = dict_list[i]  # Assigns dictionaries in the list
                    key = key_dict["Health"]  # Assigns the "Health" value of the dictionary to sort
                    # Move elements of dict_list[0..i-1], that are greater than key, to one position ahead of their current position
                    j = i - 1
                    key_dict2 = dict_list[j]  # Assigns dictionaries (characters to compare)
                    while j >= 0 and key < key_dict2["Health"]:
                        dict_list[j + 1] = key_dict2
                        j -= 1
                        key_dict2 = dict_list[j]  # Assigns dictionaries (characters to compare)
                    dict_list[j + 1] = key_dict

            # Order descending
            elif order == "D":
                # Traverse 1 through len(dict_list)
                for i in range(1, len(dict_list)):
                    key_dict = dict_list[i]  # Assigns dictionaries in the list
                    key = key_dict["Health"]  # Assigns the "Health" value of the dictionary to sort
                    # Move elements of dict_list[0..i-1], that are greater than key, to one position ahead of their current position
                    j = i - 1
                    key_dict2 = dict_list[j]  # Assigns dictionaries (characters to compare)
                    while j >= 0 and key > key_dict2["Health"]:
                        dict_list[j + 1] = key_dict2
                        j -= 1
                        key_dict2 = dict_list[j]  # Assigns dictionaries (characters to compare)
                    dict_list[j + 1] = key_dict
        else:
            print("'Health' key is not present")
    return dict_list


#==========================================#
# Place your sort_characters_armor_bubble function after this line

def sort_characters_armor_bubble(sortee: list[dict], option: str) -> list[dict]:
    """Return a list of dictionaries sorted by Armor value. It is
    sorted ascending when option = 'A', and descending when option = 'D'
    If the Armor key isn't in a dictionary, returns the input list and an error.
    >>> sort_characters_armor_bubble([{'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6,
                  'Personality': 9, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 14},
                 {'Strength': 10, 'Agility': 15, 'Stamina': 6, 'Personality': 8,
                  'Intelligence': 12, 'Luck': 0.89, 'Armor': 12, 'Weapon': 'Handaxe'},
                 {'Occupation': 'WA', 'Agility': 10, 'Stamina': 6, 'Personality': 9,
                  'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}], "A")
    [{'Occupation': 'WA', 'Agility': 10, 'Stamina': 6, 'Personality': 9,
    'Intelligence': 9,'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'},
    {'Strength': 10,'Agility': 15, 'Stamina': 6, 'Personality': 8,
    'Intelligence': 12,'Luck': 0.89, 'Armor': 12, 'Weapon': 'Handaxe'},
    {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6,
    'Personality': 9,'Intelligence': 9, 'Luck': 0.44, 'Armor': 14}]

    >>> sort_characters_armor_bubble([{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9,
                  'Personality': 10, 'Intelligence': 8, 'Armor': 14, 'Weapon': 'Spear'},
                 {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9,
                  'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 8, 'Weapon': 'Spear'},
                 {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10,
                  'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}], "D")
    [{'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9,
    'Personality': 10, 'Intelligence': 8, 'Armor': 14, 'Weapon': 'Spear'},
    {'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10,
    'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'},
    {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9,
    'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 8, 'Weapon': 'Spear'}]

    >>> sort_characters_armor_bubble([{'Luck': 0.62}])
    The "Armor" key is not present in the dictionary.
    [{'Luck': 0.62}]

    """
    finish = False
    for i in range(len(sortee)):
        if sortee[i].get("Armor") == None:
            print('The "Armor" key is not present in the dictionary.')
            finish = True
    while finish == False:
        finish = True
        for i in range(len(sortee) - 1):
            if sortee[i].get("Armor") > sortee[i + 1].get("Armor") and option == "A":
                temp = sortee[i]
                sortee[i] = sortee[i + 1]
                sortee[i + 1] = temp
                finish = False
            elif sortee[i].get("Armor") < sortee[i + 1].get("Armor") and option == "D":
                temp = sortee[i]
                sortee[i] = sortee[i + 1]
                sortee[i + 1] = temp
                finish = False
    return sortee


#==========================================#
# Place your sort function after this line

def sort(lst: list[dict], order: str, attribute: str) -> list[dict]:
    """Return a list of characters as dictionaries, ordered in ascending or descending order, according to an attribute specified by user input.
    
    Preconditions: attribute == "Agility" or attribute == "Health" or attribute == "Intelligence" or attribute == "Armor"
    >>> sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D", "Agility")
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]
    >>> sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A", "Stamina"))
    Cannot be sorted by "Stamina"
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]
    """
    try:
        if attribute == "Agility":
            return sort_characters_agility_bubble(lst, order)
        elif attribute == "Intelligence":
            return sort_characters_intelligence_selection(lst, order)
        elif attribute == "Health":
            return sort_characters_health_insertion(lst, order)
        elif attribute == "Armor":
            return sort_characters_armor_bubble(lst, order)
        else:
            raise KeyError      # if attribute is something else than the 4 listed above, go to except block

    except KeyError:
        print(f'Cannot be sorted by "{attribute}"')
        return lst

# Do NOT include a main script in your submission


