# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:51:56 2023

@author: Student
"""

import pickle
studentdata={}
students=int(input("Enter no of students"))
myfile=open("dax.dat","wb")
for i in range(students):
    studentdata["Rollno"]=int(input("Enter Rollno:"))
    studentdata["Name"]=int(input("Enter Name:"))
    studentdata["Marks"]=float(input("Marks:"))
    pickle.dump(studentdata,myfile)
    studentdata={}
    myfile.close


import pickle
studentdata={}
found=0
Rollno=int(input("Enter Rollno to Search:"))
myfile=open("ss.data","rb+")
try:
  while True:
      pos=myfile.tell()
      student.data=pickle.load(myfile)
      if(studentdata['Rollno']==Rollno):
          studentdata['Marks']=float(input("Enter marks to update:"))
          myfile.seek(pos)
          pickle.dump(stuentdata,myfile)
          found=1
          
except EOFError:
 if found == 0:
  print('Student marks updated successfully')

myfile.close()

import pickle

studentdata = {}
myfile = open('dax.dat', 'rb')
try:
 while True:
  studentdata = pickle.load(myfile)
 print(studentdata)

except EOFError:
 myfile.close()
    