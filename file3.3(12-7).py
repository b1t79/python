# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:16:39 2023

@author: Student
"""

def arCalc(x,y):
    return x+y,x-y,x*y,x/y,x%y
#__main__
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
add,sub,mult,div,mod=arCalc(num1,num2)
print("Sum of given numbers:",add)
print("Subraction of given numbers:",sub)
print("Product of given numbers:",mult)
print("Divison of given numbers:",div)
print("Modulo of given numbers:",mod)