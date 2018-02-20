# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:32:42 2017
 
@author: tiger
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import random
import requests
#import MySQLdb
import pymssql
 
######??ȡ???е???ѡ?鼮ҳ??????
# ???ý???ÿ???鼮??Ӧ??ҳ??????
def get_link(soup_page):
    soup = soup_page                                           
    items = soup('div','book-mid-info')
    ## ??ȡ????
    links = []
    for item in items:
        links.append('https:'+item.h4.a.get('href'))
    return links
 
### ????ÿ?????ӣ???ȡ??Ҫ????Ϣ
 
def get_book_info(link):
    driver.get(link)
    #soup = BeautifulSoup(driver.page_source)
    #??????????????????id
    book_id=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randint(1000,9999))
    ### ????
    title = driver.find_element_by_xpath("//div[@class='book-information cf']/div/h1/em").text
    ### ????
    author = driver.find_element_by_xpath("//div[@class='book-information cf']/div/h1/span/a").text
    ###????
    types = driver.find_element_by_xpath("//div[@class='book-information cf']/div/p[1]/a").text
    ###״̬
    status = driver.find_element_by_xpath("//div[@class='book-information cf']/div/p[1]/span[1]").text
    ###????
    words = driver.find_element_by_xpath("//div[@class='book-information cf']/div/p[3]/em[1]").text
    ###????
    cliks = driver.find_element_by_xpath("//div[@class='book-information cf']/div/p[3]/em[2]").text
    ###?Ƽ?
    recoms = driver.find_element_by_xpath("//div[@class='book-information cf']/div/p[3]/em[3]").text
    ### ??????
    try :
        votes = driver.find_element_by_xpath("//p[@id='j_userCount']/span").text
    except (ZeroDivisionError,Exception) as e:
        votes=0
        print e
        pass
    #### ????
    score = driver.find_element_by_id("j_bookScore").text
    ##??????Ϣ
    info = driver.find_element_by_xpath("//div[@class='book-intro']").text.replace('\n','')
 
    return (book_id,title,author,types,status,words,cliks,recoms,votes,score,info)
 
#############???????ݵ?mysql
def to_sql(data):
    #conn=MySQLdb.connect("localhost","root","wangwust","test",charset="utf8" )
    conn=pymssql.connect(host='127.0.0.1',user='sa',password='123',database='test')
    cursor = conn.cursor()
    #sql_create_database = 'create database if not exists test'
    #cursor.execute(sql_create_database)
#    try :
#        cursor.select_db('test')
#    except (ZeroDivisionError,Exception) as e:
#        print e
    #cursor.execute("set names gb2312")
    cursor.execute('''create table test.dbo.tiger_book2(book_id bigint,
                                                    title varchar(50),
                                                    author varchar(50),
                                                    types varchar(30),
                                                    status varchar(20),
                                                    words varchar(20),
                                                    cliks varchar(20),
                                                    recoms varchar(20),
                                                    votes varchar(20),
                                                    score varchar(20),
                                                    info varchar(3000));''')
    cursor.executemany('insert into test.dbo.tiger_book2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',data)
    #cursor.execute('select * from test.tiger_book2 limit 5;')
 
    conn.commit()
    cursor.close()
    conn.close()

#####????ÿ??ӰƬ?Ľ???ҳ????ȡ??Ϣ
base_url = "https://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page="
links = []
Max_Page = 1
rank = 0
 
for page in range(1, Max_Page+1):
    print "Processing Page ",page,".Please wait..."
    CurrentUrl = base_url + unicode(page) + u'&month=-1&style=1&action=-1&vip=-1'
    CurrentSoup = BeautifulSoup(requests.get(CurrentUrl).text,"lxml")
    links.append(get_link(CurrentSoup))
    #sleep(1)
 
#print links[9][19]
 
### ?????????鼮??Ϣ
books = []
rate = 1
driver = webdriver.PhantomJS("C:\Python27\phantomjs.exe")
 
for i in range(0,Max_Page):
    for j in range(0,20): 
        try:
            print "Getting information of the",rate,"-th book."
            books.append(get_book_info(links[i][j]))
            #sleep(0.8)
        except Exception,e:
            print e
 
        rate+=1
    if i % 15 ==0 :
            driver.quit()
            #д?????ݿ?
            to_sql(books)
            books=[]
            driver = webdriver.Firefox()
 
driver.quit()
to_sql(books)
 ###????id
#n=len(books)
#books=zip(*books)
#books.insert(0,range(1,n+1))
#books=zip(*books)
##print books[198]