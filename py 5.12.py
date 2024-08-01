# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:01:41 2023

@author: Student
"""

import pickle
emp={}
empfile=open('Emp.dat','rb')
try:
    print("FileStu.dat stores these records")
    while true:
        stu=pickle.load(fin)
        print(stu)
    except EOFError:
        fin.close()