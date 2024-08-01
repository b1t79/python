# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:25:20 2023

@author: Student
"""

fileout=open("Marks.det","a")
for i in range(2):
    print("enter details for student",(i+1),"below:")
    rollno=int(input("Rollno:"))
    name=input("Name:")
    marks=float(input("Marks:"))
    rec=str(rollno)+","+name+","+str(marks)+'/n'
    fileout.write(rec)
    fileout.close()