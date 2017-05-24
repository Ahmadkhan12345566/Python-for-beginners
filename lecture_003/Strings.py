# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:52:54 2017

@author: Ahmad khan
"""
"""
Sequnce of characters
python alows either use single qoutes ('') or doube qoutes double qoutes ("") 

"""
#string with siungle
s1='sigleqoutes'
print('single qoutes : ',s1)

#string with double qoutes
s2="Doubleqoutes"

print("doubleqoutes : ",s2)

"""
slcie is a handy way to get sub string 
syntax stringname[start:end]
  start is the from where to start 
  end is where to end

"""

#print sub string the char of 0 index only

print(s1[0:1])


#print sub a sub string


print(s1[1:5])

#how to copy  the sequence of string in  python in a new  string

s3=s1[:]


print(s3)

#use of ( % ) like in C language
 
text="%d is num  "%(45)


print(text)



