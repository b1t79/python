# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 12:18:06 2023

@author: Student
"""

import pickle
stu={}
found=False
fin=open('Stu.dat','rb')
searchkeys=[12,14]

#read from the file
try:
    print("Searching in FileStu.dat...")
    while True:
        stu=pickle.load(fin)
        if stu['Rollno'] in searchkeys:
            print(stu)
            found=True
except EOFError:
            if found==False:
                print("No such records found in the file")
            else:
                print("Search successful.")
                fin.close()  #close file