# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:48:05 2017

@author: Ahmad khan
"""

"""
Functions:
    
    built In Function
    User
    
    
   function block begin with key word def followed by function name and parentheses 
   code start with {:}
   

"""
#without paramters
def functionname():
    "functon_docstring"
    #function_suite
    return
#with parameters
def printme(str):
    "this  is print function"#this shows when you help(function name)
    print(str)
    return
printme("i am calling you")

help(printme)#this shows syntaxt and function statment

def changeme(mylist):
    "This changes a passed list into function"
    print("Values inside the function before change : ",mylist)
    
    mylist[2]=50
      
    print("values  inside the function after change : ",mylist)
    
    
def checkingkeyword(int):
    print("this")
    
    
checkingkeyword(1)