# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jack Tremblay-Lessard"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101322254"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-028"

#==========================================#
# Place your script for your batch_UI after this line

from load_data import *
from sort import *
from curve_fit import *
from histogram import *

file_input = input("Please enter the name of the file where your commands are stored: ")
file = open(file_input, 'r')

for line in file:
    line = line.strip().split(';')
    if line[0] == "L":
        #data_file = open(line[1])
        #data_file.close()
        if line[2] == "All":
            attribute = line[2], 0
        else:
            attribute = line[2], line[3]
        data = calculate_health(load_data(line[1], attribute))
        print("Data loaded")
    if line[0] == "S":
        sorted_data = sort(data, line[2], line[1])
        print("Data sorted")
        if line[3] == "Y":
            print(sorted_data)
    if line[0] == "C":
        print(curve_fit(data, line[1], int(line[2])))
    if line[0] == "H":
        histogram(data, line[1])
    if line[0] == "E":
        break
    
file.close()
