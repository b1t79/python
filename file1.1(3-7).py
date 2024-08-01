# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:56:18 2023

@author: Student
"""

fileout=open("student.txt","w")
for i in range(5):
    name=input("enter name")
    fileout.write(name)