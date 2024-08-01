# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:10:33 2023

@author: Student
"""

import pickle
st=""
with open("myfile.info","rb") as fh:
    st=pickle.load(fh)
    lst=st.split('o')
    print(lst[0])