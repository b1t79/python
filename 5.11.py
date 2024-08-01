# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:55:43 2023

@author: Student
"""

def WordsSeparated():
    try:
        myfile = open("python.txt", "r")
        lines = myfile.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                print(word + '#', end=" ")
            print()
        myfile.close()
    except FileNotFoundError:
        print("File 'python.txt' not found.")

WordsSeparated()

