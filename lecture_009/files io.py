# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:09:59 2017

@author: Ahmad khan

"""
import os
#writing in file
my_file=open('my_data.txt','w')
my_file.write('we are writing from code')
my_file.close()


new_file=open('my_data.txt','r')
data=new_file.read(10)
print(data)

#tell() currently possition 
#seek() change the position of pointer
print( new_file.tell())
"""first argument take the crrunt possition from where to move if you in enter 0 then it move from the start and when enter 1 it move from the crrunt possition""" 

print(new_file.seek(0,0))
new_file.close()


#rename() file
os.rename('my_data.txt','edited_data.txt')


#mkdir() creating new folder
os.mkdir("creating_new_file")
#chdir() moving from 1 folder to another
