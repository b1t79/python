# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:09:19 2023

@author: Student
"""

import pickle

def write_student_data():
 try:
  with open("student_data.dat", "ab") as file:
   while True:
    roll_no = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

# Create dictionary to hold student data
    student_data = {"Roll No.": roll_no, "Name": name, "Marks": marks}

# Write student data to binary file
    pickle.dump(student_data, file)

    choice = input("Do you want to enter more student data? (y/n): ")
    if choice.lower() != "y":
     break

 except OSError:
  print("Error: Failed to open or create the file.")

if __name__ == "__main__":
 write_student_data()