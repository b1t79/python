# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:57:15 2023

@author: Student
"""

import pickle
stu={}   #declare empty dictionary object to hold read records  
found=False
print("Searching in file Stu.dat...")
#open binary file in read mode and process with the with block
with open('Stu.dat','rb') as fin:
    stu=pickle.load(fin)
    if stu['Marks']>81:
        print(stu)
        found=True
        if found==False:
            print("No records with marks>81")
        else:
            print("Search successful.")