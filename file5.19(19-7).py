# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:20:08 2023

@author: Student
"""

import csv
fh=open("student.csv","w")
stuwriter=csv.writer(fh)
stuwriter.writerow(["roll no","name","marks"])
for i in range(5):
    print("student record",(i+1))
    rollno=int(input("enter roll no:"))
    name=input("enter name:")
    marks=float(input("enter marks"))
    sturec=[rollno,name,marks]
    stuwriter.writerow(sturec)
    fh.close()   #close the file