# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:26:54 2023

@author: Student
"""

import csv
fh=open("compresult.csv","w")
cwriter=csv.writer(fh)
compdata=[
    ['Name','Points','Rank'],
    ['Shradha',4500,23],
    ['Nischay',4800,31],
    ['adi',4500,25],
    ['ali',5100,14]]
cwriter.writerows(compdata)
fh.close