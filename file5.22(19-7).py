# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:45:14 2023

@author: Student
"""

import csv
with open("compresult.csv","r",newline='\r\n') as fh:
    creader=csv.reader(fh)
    for rec in creader:
        print(rec)