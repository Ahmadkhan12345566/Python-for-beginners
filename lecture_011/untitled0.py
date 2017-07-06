# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 04:13:16 2017

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
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)

#print (page.read())

soup = BeautifulSoup(page)

#print(soup.prettify())

#print(soup.title)
#print(soup.title.string)

#mystr = soup.title.string
#ls = mystr.split()
#print(ls)

a_tags = soup.find_all('a')

#right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
right_table=soup.find('table', {'class': 'wikitable sortable plainrowheaders'})

table_list = list(right_table)

print(len(table_list))

print(table_list[:2])

new_list = table_list[:]
new_list.remove('\n')
print(new_list[:2])
