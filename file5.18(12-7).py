# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:11:01 2023

@author: Student
"""

import pickle
stu={}
found=False
fin=open('Stu.dat','rb+')
# red from the file
try:
    while True:
        rpos=fin.tell()
        stu=pickle.load(fin)
        if stu['rollno']==12:
            stu['Name']='Gurnam'
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
except EOFError:
        if found==False:
                print("Sorry, no matching reacord found")