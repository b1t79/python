# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:03:46 2023

@author: Student
"""

import pickle
stu={}    # declare empty dictionary object to hold read records
found=False
#open binary file in read and write mode
fin=open('Stu.dat','rb+')
#read from the file
try:
    while True:
        rpos=fin.tell()
        stu=pickle.load(fin)
        
        if stu['Marks']>81:
            stu['Marks']+=2
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
except EOFError:
    if found==False:
        print("Sorry, no matching record found")
    else:
        print("Record(s) succesfully updated.")
        fin.close()   #close file
        