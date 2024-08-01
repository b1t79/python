# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:14:14 2023

@author: Student
"""

import pickle
stu={}
found=False
print("searching in file stu.dat...")
with open ('stu.dat','rb')as fin:
    stu=pickle.load(fin)
    if stu['marks']>81:
        print(stu)
        found=True
        if found==False:
            print("no records with marks>81")
        else:
            print('search successful.')
        