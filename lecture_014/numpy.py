"""
Created on Tue Jul 18 22:35:48 2017

@author: Ahmad khan
"""

import numpy as np
a=np.arange(30).reshape(2,3,5)#set the number of row and columns and 
print(a)
print('num of rows and colums',a.shape)#find number of rows and cloumns
print('dimenssions',a.ndim)
print('Size of  a single item',a.itemsize)
b=np.array([[1,2,3],[1,2,3]])
print(b)
y=np.linspace(0,2,15)
print(y)
g =3*np.ones((3,3))
print("g",g)