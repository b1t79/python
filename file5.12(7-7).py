# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:41:45 2023

@author: Student
"""

import pickle
stu={}
fin=open('Stu.dat','rb')
#read from the file
try:
    print("File Stu.data stores these records")
    while True :
        stu=pickle.load(fin)
        print(stu)
except EOFError:
        fin.close()