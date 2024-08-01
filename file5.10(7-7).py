# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:19:10 2023

@author: Student
"""

import pickle
#declare empty dictionary
stu={}
#open file in append mode
stufile=open('Stu.data','ab')
#get data to write onto the file
ans='y'
while ans=='y':
    rno=int(input("Enter roll number"))
    name=input("Enter name:")
    marks=float(input("Enter marks"))
    #add read data into dictionary
    stu['Roll no']=rno
    stu['Marks']=marks
    #now write into the file
    pickle.dump(stu,stufile)
    ans=input("Want to append more records?(y/n)...")
    #close file
    stufile.close