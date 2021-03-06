# coding: utf-8

import requests
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd

start  = time.time()



url = 'https://www.classtok.net/modoo/start_now'
response = requests.get(url)
response



soup = BeautifulSoup(response.content, 'html.parser')
soup



elements = soup.select('body > div.main_wrap > div > div > ul > div > li > div > a.product_info')
len(elements)



links = []
for i in range(len(elements)):
    links.append('https://classtok.net' + str(elements[i]).replace('<a class="product_info" href="', '').split('">\n<span>')[0])
len(links)



#site, title, category_2, teacher, price, discount, likes, link



onetime = []
datas = []

for element in elements:
    
    site = '클래스톡'
    try:
        likes = element.select_one('.product_star').text.split()[0]
    except:
        likes = ''
    
    datas.append({
        "site" : site,
        "title" : element.select_one('h2').text,
        "category_2" : element.select_one('span').text.split(' · ')[0],
        "teacher" : element.select_one('span').text.split(' · ')[1],
        "price" : element.select_one('.price_info').text.split('\n')[1],
        "discount" : element.select_one('.price_info').text.split('\n')[2].replace(' 할인',''),
        "likes" : likes,
        "link" : 'https://www.classtok.net' + element.get('href'),
    })
    onetime.append(datas)
classtok_df = pd.DataFrame(datas)
classtok_df.tail()



classtok_df = classtok_df.append(onetime)
print('time: ', round((time.time() - start)/60, 1), '분', sep='')
print('\n')



classtok_df.to_csv(f'./classtok_{datetime.datetime.now().strftime("%y%m%d%H%M%S")}.csv', encoding='utf-8')


print('전체')
print('time: ', round((time.time() - start)/60, 1), '분', sep='')
print('\n')
print('total: ', len(classtok_df), sep='')


