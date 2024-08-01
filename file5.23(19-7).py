# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:46:20 2023

@author: Student
"""

import csv

with open("Employee.csv","w",newline='') as fh:
    ewriter=csv.writer(fh)
    empdata=[
        ['Empno','Name','Designation','Salary'],
        ['1001','Trupti','Manager','56000'],
        ['1002','Raj','Manager','55900'],
        ['1003','Sianager','Manager','55900'],
        ['1004','Raj','Manager','55900'],
        ['1005','Saket','Manager','5900'],
         ]
    ewriter.writerows(empdata)
    print("File succesfully created")
    fh.close()
         

         
        