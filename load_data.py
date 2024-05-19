# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Aya Skinner, Rayane Boussanni, Jack Tremblay-Lessard, Emma Tovell Baudier"

# Update "" with your team (e.g. T102)
__team__ = "T-028"


#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list(file_name: str, character_occupation: str) -> list[dict]:
    """Returns any Pokemon character's information that has a particular occupation read from an inputted file.
    
    >>> character_occupation_list("characters-mat.csv", "AT")
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 
    'Intelligence': 8, 'Luck': '0.67', 'Armor': 8, 'Weapon': 'Staff'}, {ect}]
    
    >>> character_occupation_list("characters-mat.csv", "DB")
    [{'Strength': 17, 'Agility': 5, 'Stamina': 10, 'Personality': 11, 'Intelligence': 11, 
    'Luck': '0.67', 'Armor': 9, 'Weapon': 'Club'}, {'Strength': 9, 'Agility': 9, 
    'Stamina': 3, 'Personality': 13, 'Intelligence': 15, 'Luck': '0.5', 'Armor': 10, 'Weapon': 'Club'}, {ect}]
    
    >>> character_occupation_list("characters-mat.csv", "XXXX")
    []
    """

    # set a counter to track the row number
    counter = 0
    # open the file from the user and assign in to in_file
    in_file = open(file_name, "r")
    # create a list to add the dictionnary values of the corresponding occupation
    occupation_list = []
    # iterate through each line of the file
    for line in in_file:
        # remove any whitespace
        line = line.strip()
        # put a comma between each word
        line = line.split(',')
        # print(line)
        if counter == 0:
            # create the name of the header from the first line
            table_header = line
        else:
            # add the value of the dictionnary to the list
            game_char = {}
            game_char[table_header[0]] = line[0]
            game_char[table_header[1]] = int(line[1])
            game_char[table_header[2]] = int(line[2])
            game_char[table_header[3]] = int(line[3])
            game_char[table_header[4]] = int(line[4])
            game_char[table_header[5]] = int(line[5])
            game_char[table_header[6]] = float(line[6])
            game_char[table_header[7]] = int(line[7])
            game_char[table_header[8]] = line[8]

            # check to see if the value of the key is equal to the value passed in by the user
            if game_char[table_header[0]] == character_occupation:
                del game_char["Occupation"]
                occupation_list.append(game_char)

        counter += 1

    # close the file
    in_file.close()
    # return an empty list
    return(occupation_list)

#==========================================#
# Place your character_strength_list function after this line


def character_strength_list(csv_file: str, strength_range: tuple[int, int]) -> list[dict]:
    """returns a dictionnary of characters (stored as a dictionary) whose strength falls between the minimum and maximum values, inclusive, that were
provided as an input parameter from the given csv file.
    >>> character_strength_list ('characters-mat.csv', (8, 11))
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8,
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9,
     'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'},
    {another element},
     …
    ]
    >>> character_strength_list ('characters-mat.csv', (1000, 10001))
    []
    """
    file = open(csv_file, 'r')
    character_list = []

    for index, line in enumerate(file):
        split_line = line.strip().split(',')
        strength = split_line.pop(1)  # remove strength from the data

        if index == 0:
            labels = split_line  # get labels from the first line

        # check if strength is in the range
        elif strength_range[0] <= int(strength) <= strength_range[1]:
            character_list.append({             # append each stat to the character list
                labels[0]: split_line[0],
                labels[1]: int(split_line[1]),
                labels[2]: int(split_line[2]),
                labels[3]: int(split_line[3]),
                labels[4]: int(split_line[4]),
                labels[5]: float(split_line[5]),
                labels[6]: int(split_line[6]),
                labels[7]: split_line[7],
            })

    file.close()
    return character_list

#==========================================#
# Place your character_luck_list function after this line


def character_luck_list(file: str, maximum_luck: float) -> list[dict]:
    """Return a list of dictionaries of character stats (from the input file)
    with a luck less than maximum_luck. The luck value of each character is not 
    included in the dictionary.
    >>> character_luck_list("characters-mat.csv", 1)
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Armor': 8, 'Weapon': 'Staff'},
    {other values}
    ...
    ]
    >>> character_luck_list("characters-mat.csv", 0)
    []
    """
    final_character_list = []
    data_file = open(file, "r")
    data = data_file.read().split("\n")
    types = data.pop(0).split(",")
    for i in data:
        raw_data = i.split(",")
        if float(raw_data[6]) < maximum_luck:
            this_character = {}
            for x in range(len(types)):
                if x == 0 or x == 8:
                    this_character[types[x]] = raw_data[x]
                elif x == 6:
                    pass  # The luck value is not added to the dictionary
                else:
                    this_character[types[x]] = int(raw_data[x])
            final_character_list.append(this_character)
    data_file.close()
    return final_character_list

#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, weapon_value: str) -> list[dict]:
    """Returns a list containing the characters that have a particular weapon in the form of dictionaries containing all their attributes other than their weapon.

    Preconditions: None.

    >>> character_weapon_list("characters-mat.csv", "aaa")
    []
    >>> character_weapon_list("characters-mat.csv", "Staff")
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8}, {etc}]
    >>> character_weapon_list("characters-mat.csv", "Dagger")
    [{'Occupation': 'AT', 'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9}, {etc}]
    """
    in_file = open(file_name, 'r')
    first_line = True #Checks if its reading the first line of the document
    final_list = []
    for line in in_file:
        line = line.strip().split(',') #Clean up line and separate elements into list
        if first_line:
            first_line = False #All the other rows are not headers
            table_header = line #Set the first line as the header
        else:
            character = {} #Create empty dictionary for character information
            #Sets the key as the header and the value as the value of said header for the character
            character[table_header[0]] = line[0]
            character[table_header[1]] = int(line[1])
            character[table_header[2]] = int(line[2])
            character[table_header[3]] = int(line[3])
            character[table_header[4]] = int(line[4])
            character[table_header[5]] = int(line[5])
            character[table_header[6]] = float(line[6])
            character[table_header[7]] = int(line[7])
            if line[8] == weapon_value: #If the weapon value provided matches the weapon of the character, do body
                final_list.append(character) #Append the character dictionary to the final list
    in_file.close()
    return final_list

#==========================================#
# Place your load_data function after this line

# the inputs of the tuple vary in length and type


def load_data(file_name: str, character_identity: tuple) -> list[dict]:
    """Return a list of dictionaries of the characters, taken from a csv file (file_name), that have the attribute and corresponding value outlined in character_identity. The attribute used for loading the data is not included in each character's dictionary.
    >>>load_data("characters-mat.csv", ("Weapon", "Staff"))
     [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Armor': 8},
    {other values}
    ...
    ]
    >>>load_data("characters-mat.csv", ("All", 3))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
    {other values}
    ]
    >>>load_data("characters-mat.csv", ("Magic", 4))
    Invalid Type

    """
    character_list = []
    # if the user wants to see all the data
    if character_identity[0] == "All":

        # set a counter to track the row number
        counter = 0
        # open the file from the user and assign in to in_file
        in_file = open(file_name, "r")

        # iterate through each line of the file
        for line in in_file:
            # remove any whitespace
            line = line.strip()
            # put a comma between each word
            line = line.split(',')
            # print(line)
            if counter == 0:
                # create the name of the header from the first line
                table_header = line
            else:
                # add the value of the dictionnary to the list
                game_char = {}
                game_char[table_header[0]] = line[0]
                game_char[table_header[1]] = int(line[1])
                game_char[table_header[2]] = int(line[2])
                game_char[table_header[3]] = int(line[3])
                game_char[table_header[4]] = int(line[4])
                game_char[table_header[5]] = int(line[5])
                game_char[table_header[6]] = float(line[6])
                game_char[table_header[7]] = int(line[7])
                game_char[table_header[8]] = line[8]
                character_list.append(game_char)
            counter += 1
        # print(game_char)
        in_file.close()
    # for character occupation
    elif character_identity[0] == "Occupation":
        character_list = character_occupation_list(
            file_name, character_identity[1])
    # character strength, calls the character_strength_list funciton
    elif character_identity[0] == "Strength":
        character_list = character_strength_list(
            file_name, (character_identity[1][0], character_identity[1][1]))
    # character luck
    elif character_identity[0] == "Luck":
        character_list = character_luck_list(
            file_name, character_identity[1])

    # character weapon
    elif character_identity[0] == "Weapon":
        character_list = character_weapon_list(
            file_name, character_identity[1])
    # user entered an invalid value
    else:
        print("Invalid Value")

    return character_list


#==========================================#
# Place your calculate_health function after this line
def calculate_health(character_list: list[dict]) -> list[dict]:
    """Returns a list with the dictionaries updated with the characters’ health given a list of character dictionaries.
    
    >>> calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6,'Personality': 7, 'Intelligence': 8, 'Luck': 0.7, 'Armor': 8, 'Weapon': 'Staff'}])
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,'Intelligence': 8, 'Luck': 0.7, 'Armor': 8, 'Weapon': 'Staff', 'Health': 80.8}]
    >>> calculate_health([{'Strength': 1, 'Agility': 2, 'Stamina': 0,'Personality': 19, 'Intelligence': 2, 'Luck': 1, 'Armor': 1, 'Weapon': 'Staff'}])
    [{'Strength': 1, 'Agility': 2, 'Stamina': 0, 'Personality': 19,'Intelligence': 2, 'Luck': 1, 'Armor': 1, 'Weapon': 'Staff', 'Health': 25}]
    >>> calculate_health([{'Strength': 0, 'Agility': 0, 'Stamina': 0,'Personality': 0, 'Intelligence': 0, 'Luck': 0, 'Armor': 0, 'Weapon': 'Staff'}])
    [{'Strength': 0, 'Agility': 0, 'Stamina': 0,'Personality': 0, 'Intelligence': 0, 'Luck': 0, 'Armor': 0, 'Weapon': 'Staff', 'Health': 0}]


    """
    for character in character_list:
        character['Health'] = (character['Strength'] +
                               character['Agility'] +
                               character['Stamina'] +
                               character['Personality'] +
                               character['Intelligence'] +
                               (character['Armor'] ** 2) * character['Luck']
                               )
    return character_list

# Do NOT include a main script in your submission
