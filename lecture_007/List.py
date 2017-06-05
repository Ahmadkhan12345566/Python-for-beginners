# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 22:23:57 2017

@author: Ahmad khan
"""
my_ints=[4,3,4,5,6,43,32,0]
another_list=list(range(500))
#displaying list
print(my_ints)

duplist_list=my_ints
duplist_list[2]=700
my_ints.insert(10,10)#insert a value to specific idex
my_ints.append(546)#adding new element to list 
print("orignal",my_ints)
print("dplicate",duplist_list)



