# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:47:27 2023

@author: Student
"""

import pickle
stu={}
stufile=open('stu.dat','ab')
ans='y'
while ans=='y':
    rno=int(input("Enter roll number:"))
    name=input("enter name:")
    marks=float(input("enter marks:"))
    stu['rollno']=rno
    stu['name']=name
    stu['marks']=marks
    pickle.dump(stu,stufile)
    ans=input("want to append more records?(y\n)...")
    stufile.close()
 

    