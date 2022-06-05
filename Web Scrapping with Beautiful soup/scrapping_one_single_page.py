from sys import unraisablehook
from urllib import response
import requests
from bs4 import BeautifulSoup
url='http://quotes.toscrape.com/'
response=requests.get(url)
response = BeautifulSoup(response.text,'lxml') 
quotes=response.find_all('span',class_='text')
authors=response.find_all('small',class_='author')
tags=response.find_all('div',class_='tags')
for i, quote in enumerate(quotes):
        print(f'{quote.text} \n Author: {authors[i].text}' )
        quote_tags = tags[i].find_all('a',class_='tag')
        print(' Tags:')
        for tag in quote_tags:
            print('   '+ tag.text)