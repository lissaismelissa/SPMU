# -*- coding: utf8 -*-
import requests
import re
from bs4 import BeautifulSoup
import sqlite3


def request(new_url):
    data = requests.get(new_url).text
    soup = BeautifulSoup(data, features="html.parser")
    return soup

def brackets(text):
    text = re.sub("\[.*?\]","", text)
    text = text.replace('́', '')
    return text


url = "https://ru.wikipedia.org"
wiki = "/wiki/"
url_title = ["Категория:Выпускники_Санкт-Петербургского_горного_университета",
"Категория:Выпускники_Горного_кадетского_корпуса","Категория:Выпускники_института_Корпуса_горных_инженеров",
"Категория:Выпускники_Петербургского_Горного_училища","Категория:Выпускники_Санкт-Петербургского_горного_института_(до_1917_года)"]

#___________________имена и ссылки_____________________
n = 0
inf = []    #тут переделала списки
person = []
category = []

for info in url_title:
    new_url = url + wiki + url_title[n]            
    soup = request(new_url)
    full_list = soup.find('div', {'class': 'mw-category mw-category-columns'})
    for link in full_list.find_all('a'):           
        text = link.text.replace(',', '')
        inf.append(text.rsplit('(',1)[0])  #тут
        inf.append(url+link.get('href'))   #тут
        person.append(inf.copy())          #тут
        inf.clear()                        #тут
    category.append(person.copy())         #тут
    person.clear()                         #тут
    n += 1

#print(category)


#_____________перебор ссылок выпускников_______________

#туть убрала объявление списков

i=0
j=0

for list in category:
    j=0
    for number in list:
        new_url = category[i][j][1] #туть
        soup = request(new_url)

        full_list = soup
        flag_1 = full_list.find('div', {'class': 'toc'})
        flag_2 = full_list.find('table', {'class': 'infobox'})
        flag_3 = full_list.find('div', {'class': 'floatright'})
        flag_4 = full_list.find('div', {'class': 'thumb tright'})
 
                                                                #первый абзац (проверка исключений и поиск)
        if (flag_2 and flag_2.find_next_sibling().name == 'p'):
            text = flag_2.find_next_sibling().text
            text = brackets(text)
            category[i][j].append(text)#туть
        elif (flag_1 and flag_1.find_previous_sibling().name == 'p'):
            text = flag_1.find_previous_sibling().text
            text = brackets(text)
            category[i][j].append(text)#туть
        elif (flag_4 and flag_4.find_previous_sibling().name == 'p'):
            text = flag_4.find_previous_sibling().text
            text = brackets(text)
            category[i][j].append(text)#туть
        elif full_list.find('h2').find_previous_sibling().name == 'p':
            text = full_list.find('h2').find_previous_sibling().text
            text = brackets(text)
            category[i][j].append(text)#туть
        elif (flag_3 and flag_3.find_previous_sibling().name == 'p'):
            text = flag_3.find_previous_sibling().text
            text = brackets(text)
            category[i][j].append(text)#туть
        
        image = ''
        if full_list.find('tbody'):
            infobox = full_list.find('tbody').find_all('tr')
            for tr in infobox:
                if tr.find('td', {'class': 'infobox-image'}):
                    image = 'https:' + tr.find('img').get('src')
                    category[i][j].append(image)
        if image == '':
            category[i][j].append('https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Default-welcomer.png/800px-Default-welcomer.png')
        
        j+=1
    i+=1
print(category)
#будет выгружать несколько минут

for i in range(0,4,1):
    with sqlite3.connect("C:\\Users\\DNS\\PycharmProjects\\pythonProject\\SPMU350\\spmu\\db.sqlite3") as db:
        cursor = db.cursor()
        query = """ INSERT INTO columns_list_columns (title, link, info, photo) VALUES(?, ?, ?, ?); """ #добавление данных
        cursor.executemany(query, category[i]) #добавление данных
        db.commit()