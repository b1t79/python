# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:00:36 2023

@author: Student
"""

filename = input("Enter the file name: ")
with open(filename, 'r') as f:
    text = f.read()
    vowels = 0
    consonants = 0
    for i in text:
        if i.isalpha():
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
