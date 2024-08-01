# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:06:26 2023

@author: Student
"""

import pickle
string="this is my first line.this is second line."
with open("myfile.info","wb")as fh:
    pickle.dump(string,fh)
print("file successfully,fh")