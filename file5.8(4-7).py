# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:46:48 2023

@author: Student
"""


import pickle

# dictionary objects to be stored in binary file
emp1={'empno':1201,'Name':'Anushree','Age':25,'salary':47000}
emp2={'empno':1211,'Name':'Zoya','Age':30,'salary':48000}
emp3={'empno':1251,'Name':'Simarjeet','Age':27,'salary':49000}
emp4={'empno':1266,'Name':'Alex','Age':29,'salary':50000}

# open file in write mode
empfile = open('emp.dat', 'wb')

# write onto the file
pickle.dump(emp1, empfile)
pickle.dump(emp2, empfile)
pickle.dump(emp3, empfile)
pickle.dump(emp4, empfile)

print("Successfully written four dictionaries")
empfile.close() # close file