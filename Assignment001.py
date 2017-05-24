# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:52:54 2017

@author: Ahmad khan
"""

#M=int(input("Enter the montly payment : "))
L=int(input("Enter the Loan amount : "))
I=float(input("Enter the intrst rate : "))
N=int(input("Enter the number of payments : "))
print("Your Payment is : ")
print(L*(I*(1+I)*N)/(1+I)*N-1)
