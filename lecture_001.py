# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Variables


Pythone variables do not need explicit declaration 

Declaration happens auomatically when assign a value..........

"""

counter =100  #intger type 
miles=1000.0   #float type
name='Pakistan'#string
desc=False;#bool
if(desc):#
    print(name)
else:
    print(miles)
    
    
    a=b=c=20 #assigning a single value to  multiple variables
var01,var02,var03=10,3.14,'Islamabad'#assigning values to multiple variables 


"""types of data
        Number
        String(there is no consept of charcter in Pythone) 
        List
        Tuple
        Dictionary
""" 
#Number (store numeric values)

var1=1
var2=2#these are two variables of numeric type

#deleting a variable
del var01
#deleting multipet variabkles
del var02,var03
"""four types of numberical types
    int (signed integers(11))
    long (long integers(111111111111111111111111111111111))
    float(floating point real values(3.14))
    complex(complex numbers(like (iota))
"""
#int
i1=1
i2=2
#adding to int
i3=i1+i2

#complex
c1=complex(4,5)#assigning complex vlue to variable
c2=complex(4,6)


print(c1)
#adding complex numbers
print(c1+c2)
#dividing complex numbers
print(c1/c2)


##how to check descripton of a reserve word or a function
help(complex)

##how to take input

n1=input("Enter the value :  ")

"""
Python takes input in string type so when we take integer as a input we use function to conver
int()
float()

"""

##suppose we want take data of int type as a input

n1=input("Enter the value :  ")
n1=int(n1)

##suppose we want take data of float type as a input

n2=input("Enter the value :  ")
n2=float(n2)
n3=float(input("Enter your gpa    :"))#we can aslo conver as this
"""
Tpyes of Operators

    Arithmetic Operators(+,-,/,//,*,**(exponent))
    Comparison(==,!=,<>(nt eqal to),>,<,>=,<=)
    Assignment (=,+=,-=,/=,*=,%=,**=,//=)
    Bitwise Operators(&(and),|(or),^(xor),~(not),<<(left shift),>>(right shift))
    Logical Operators(and,or,not)
    Membership Operators(is,is not)
"""

#Arithmatic Operators

a1=7
a2=2
add=a1+a2
sub=a1-a2
a3=a1/a2#default answer
a4=a1//a2#ignor the floating point numbers

#Comparison
if(a1==a2):
    print (a1)
elif(a1!=a3):
    print(a3)
elif(a1<=a2):
    print(a2)
else:
    sub
    
    
    

#Assignment
as1=1;
as1+=as1
as1-=1
#Bitwise 



