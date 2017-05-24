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
    expandtab
    islower
    
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



#expandtab(increase the tab where we add \t berfor in code)

statment1="i like\tpythone "

print( "with expands",statment1.expandtabs(45))
print("without expands", statment1)

#islower (cheks the whole string is in lower case or not)


print("islower",statment1.islower());
     
     
 #isnumeric(cheks the whole string is in numeric case or not)


print("isnumeric",statment1.isnumeric())    



#isspace(cheks the whole string have case or not)

print("isspace",statment1.isspace())



#istitle
print("isspace",statment1.title())


#join(combien the sequence of strings)

s="-"
seq=("a","b","c")
print("Sequence   :   ",s.join(seq))


#len
statment2="abc"
#leng=len(statment2)
# print(len(statment1))


#ljust


print("ljust : ",statment2.ljust(20))

#rjust

print("rjust : ",statment2.rjust(20))


#lstrip(remove string from left)

print("rjust : ",statment2.lstrip("a"))

#rstrip(remove string from right)
print("rjust : ",statment2.rstrip("c"))

#translate

intab="aeiou"

outtab="12345"

trantab=str.maketrans(intab,outtab)

strnn="this is string "

print("translate  :  ",strnn.translate(trantab))

#max(print the index have gretest ascii value)
print("nmax  :  ",max(strnn))

#min(print the index have minimum ascii value)
print("nmax  :  ",min(strnn))


#replace

print("replace   : ",strnn.replace('t','r'))

#rfind (find the right msot index of this character)
print("rfind  :  ",strnn.rfind('r'))

#split(split from all places where given char occours)

print("split ",strnn.split('i'))


