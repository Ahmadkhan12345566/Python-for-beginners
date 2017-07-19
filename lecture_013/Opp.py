# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#class variable
#method overloding (same name same parameters)
class Person:
    'this is a fake class'
    a="9"#class variable
    def __init__(self ,name):
        self.name=name;#datamembers
    def xyz(self):
        self.name
        print("i in main form")
        
class Child(Person):#inharitance
    def xyz(self):
        print("i am over loded")
        #operator overloding
class vector():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return vector(self.a+other.a,self.b+other.b)
    def __str__(self):
        return ("Vector(%i ,%i)") %(self.a,self.b)
        
        
prsn=Person("khan")#object creating 
chld=Child("kh")
chld.xyz()#calling overloded function
prsn.xyz()#calling function
vec=vector(4,5)
vec2=vector(8,9)
print(vec+vec2)

       
       
       
       