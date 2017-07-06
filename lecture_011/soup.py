# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:20:38 2017

@author: Ahmad khan
"""

# -*- coding: utf-8 -*-

# Lecture 10

"""
Created on Mon Jun 12 10:38:26 2017

@author: Asad
"""

# Web Scraping


#import the library used to query a website
import urllib.request
from bs4 import BeautifulSoup 

#specify the url
wiki = "https://stackoverflow.com/questions/42357976/how-to-get-the-sum-of-two-strings-of-numbers-c"

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)

#print (page.read())

soup = BeautifulSoup(page)
#print(soup.title)
print(soup.title.string)
s=soup.title.string
mystr = soup.title.string
ls = mystr.split()
print(ls)


print("rfind  :  ",s.rfind('-'))
question=s[0:s.rfind('-')]
list_question=question.split()
site=s[(s.rfind('-')+1):]
list_site=site.split()
print("Site :    ",site)
print(list_site)
print("Question   :    ",question)
print(list_question)
print("rfind  :  ",question.rfind('-'))
#writing in file
my_file=open('tags.txt','w')
if question.rfind('-')!=-1:
    q_topic=question[(question.rfind('-')+1):]
    question_=question[0:question.rfind('-')]
    my_file.write("#"+question_+"\n")
    #print(question[(question.rfind('-')+1):])
    my_file.write("#"+q_topic+"\n")
my_file.write("#"+site+"\n")
my_file.write("#"+list_question[-1])
my_file.write("#"+question)
my_file.close()
