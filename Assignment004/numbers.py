# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:53:27 2017

@author: Ahmad khan
"""
import math 
num1=-1.11
num2=2
#It is possible to represent a number in hexa-decimal or octal form
number=0o37 #Octal
print("Octal : ",number)
#Number Type Conversion

print("int : ",int(num1))
print("complex : ",complex(num1))
#Mathematical Functions

print("abs : ",abs(num1))

print("ceil : ",math.ceil(num1))


#print("cmp : ",cmp(num1,num2) )


print("exp : ",math.exp(num2))



print("fabs : ",math.fabs(num1))
print("floor : ",math.floor(num2))
print("log : ",math.log(num2) )

print("log10 : ",math.log10(num2) )
print("max : ",max(10,11,12) )
print("min : ",min(10,11,12))

print("pow : ",math.pow(2, 4))


print("sqrt : ",math.sqrt(4))


#Random Number Functions


tup2="1","2","3"
print("choice :  ",math.choice(tup2) )