# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 23:00:21 2023

@author: Dax Patel
"""

myfile = open("answer.txt", "r")  # Open the file in read mode

line = ""  # Initialize line with an empty string

while line:
    line = myfile.readline()  # Read one line from the file
    
    # Print each word in the line, separated by '#'
    for word in line():
        print(word, end='#')
    
print()

myfile.close()  # Close the file