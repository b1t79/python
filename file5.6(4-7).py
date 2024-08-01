# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:39:46 2023

@author: Student
"""

myfile=open("*answer.txt","r")
line="" #initially stored a space (a non-None value)
while line:
    line=myfile.readline() #one line read from file
    #printing the line word by using word split()
    for word in line.split():
        print(word,end='#')
        print()
        #close the file
        myfile.close()