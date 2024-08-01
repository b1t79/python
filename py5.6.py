# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:33:38 2023

@author: Student
"""

myfile=open("Answer.txt","r")
line=""
while line:
    line=myfile.readline()
    for word in line.split():
        print(word,end='#')
        print()
        myfile.close()