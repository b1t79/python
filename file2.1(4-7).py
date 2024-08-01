# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:57:57 2023

@author: Student
"""

num_students = int(input("Enter the number of students: "))

with open("marks.txt", "w") as file:
    for i in range(num_students):
        roll_no = input("Enter the roll number of student {}: ".format(i+1))
        name = input("Enter the name of student {}: ".format(i+1))
        marks = input("Enter the marks of student {}: ".format(i+1))
        file.write("{},{},{}\n".format(roll_no, name, marks))

print("Data saved to marks.txt")
