# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:28:08 2023

@author: Student
"""

import pickle
#declare empty dictionary  object; it will hold the read record
emp={}
empfile=open('Emp.dat','rb') #open binary file in read mode
#read from the file
try:
    while True : #it will become False when the end of file is reached (EOF exception)
     emp=pickle.load(empfile)
    print(emp)
except EOFError:
    empfile.close()