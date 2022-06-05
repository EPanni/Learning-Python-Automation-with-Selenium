from urllib import response
import requests
from bs4 import BeautifulSoup
urls=[]
url='http://scrapingclub.com/exercise/list_basic/?page=1'
response=requests.get(url)
response = BeautifulSoup(response.text,'lxml') 
items=response.find_all('div',class_='col-lg-4 col-md-6 mb-4')
pages = response.find('ul',class_='pagination')
links=pages.find_all('a', class_='page-link')
for link in links:
    page_num= int(link.text) if link.text.isdigit() else None
    if page_num:
        x = link.get('href')
        urls.append(x)
count=1
for url_aux in urls:
    new_url=url[:-1]+url_aux
    response=requests.get(new_url)
    response = BeautifulSoup(response.text,'lxml') 
    items=response.find_all('div',class_='col-lg-4 col-md-6 mb-4')
    for item in items:
        item_name = item.find('h4', class_='card-title').text.strip('\n')
        item_price= item.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (count, item_price,item_name))
        count+=1