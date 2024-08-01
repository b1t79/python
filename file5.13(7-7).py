# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:07:52 2023

@author: Student
"""

import pickle
string="This is my file line. This is second line."
with open ("my file.info","wb") as fh:
    pickle.dump(string,fh)
    print("File succesfully created.")