# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:36:21 2023

@author: Student
"""

myfile=open("Answer.txt","r")
ch=""
vcount=0
ccount=0
while ch:
    ch=myfile.read(1)
    if ch in['a','A','e','E','i','I','o','O','u','U']:
        vcount=vcount+1
    else:
        ccount=ccount+1
print("vowels in the file:",vcount)
print("consonants in the file:",ccount)
myfile.close()

        