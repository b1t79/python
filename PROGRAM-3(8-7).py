# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:44:56 2023

@author: Student
"""

fileout=open("kavya.txt","r")
fn=open("kavyam.txt","w")
f1=open("kavya2.txt","w")
lines=fileout.readlines()
l=[]
for line in lines:
    if 'a' in line:
        fn.write(line)
        
        
        for line in lines:
            if not'a' in line:
                f1.write(line)
                
                
                fileout.close()
                fn.close