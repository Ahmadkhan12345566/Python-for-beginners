# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:35:31 2017

@author: Ahmad khan
"""

"""
Some Built-in Methods
    capitalize
    center
    count
    endswith
    startwith
    find
    isalnum
    isalpha
    index
    istitle
    min
    center
    rindex

"""
#  capitalize(return the first character with (capital letter))

str1="this is proper noun"
print ("Capital :", str1.capitalize())

# cenert(return centerd in string of width length)

print ("center :", str1.center(50))#,'*'

      
#count  (count how many times a substring occours in string)

print("count :",str1.count('p'))      

#endswith(it check the end of string suffix and return bool dessions)


print('endswith   : ',str1.endswith('n'))



#startwith(check the starting point and return bool dession)

print("startswith   :" ,str1.startswith('t'))

#find (check if the string occours in a string return the index where occours)  when not found retun it retun (-1)
#but there is no space in string
str6="pythonisafrandlyprograminglangage3453"

print("Find ",str6.find('f'))

#isalnum(checks the given value is alfanumeric or numeric )
str8="khan786"

print("isalnum",str8.isalnum())


#isalpha(checks the given string is alpahabet or not return bool dessions)
alpha="ahmad"
print("alpha   :",alpha.isalpha())