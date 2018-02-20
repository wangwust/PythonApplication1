from bs4 import BeautifulSoup 
import requests 
import time 

url = 'https://knewone.com/things/?page=' 
#html = """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>

#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>

#<p class="story">...</p>
#"""
#soup = BeautifulSoup(html,'html.parser') 
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)
#print(soup.find_all('p'))

#aList = soup.find_all('a')
#for link in aList:
#    print(link.get('href'))

#print(soup.get_text())

#print(soup.prettify())

def get_page(url,data=None): 
    wb_data = requests.get(url) 
    soup = BeautifulSoup(wb_data.text,'lxml') 
    imgs = soup.select('a.cover-inner > img') 
    titles = soup.select('section.content > h4 > a') 
    links = soup.select('section.content > h4 > a') 
    if data == None: 
        for img,title,link in zip(imgs,titles,links): 
            data = { 
                'img':img.get('src'), 
                'title':title.get('title'), 
                'link':link.get('href') } 
            print(data) 

def get_more_pages(start,end): 
    for one in range(start,end): 
        get_page(url + str(one)) 
        time.sleep(1) 


try:
    get_more_pages(1,8);
except e:
    print(e.message)

