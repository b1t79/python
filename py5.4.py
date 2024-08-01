# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:24:56 2023

@author: Student
"""

fileout=open("marks.txt","a")
for i in range(2):
    print("enter details for student",(i+1),"below:")
    rollno=int(input("enter the rollno:"))
    name=input("name:")
    marks=float(input("marks:"))
    rec=str(rollno)+","+name+","+str(marks)+'\n'
    fileout.write(rec)
    fileout.close()