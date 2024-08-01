# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:10:17 2023

@author: Student
"""

import pickle
st=''
with open("myfile.info","rb")as fh:
    st=pickle.load(fh)
    lst=st.split('o')
    print(lst[0])