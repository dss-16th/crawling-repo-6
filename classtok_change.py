
import requests
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd

start  = time.time()



url = 'https://www.classtok.net/modoo/start_now'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
elements = soup.select('body > div.main_wrap > div > div > ul > div > li > div > a.product_info')

links = []
for i in range(len(elements)):
    links.append('https://classtok.net' + str(elements[i]).replace('<a class="product_info" href="', '').split('">\n<span>')[0])

classtok_df = pd.DataFrame(columns=['site', 'link', 'title', 'teacher', 'category_1', 'category_2', 's_price', 'discount', 'contentment'])

onetime = []

for element in elements:
    
    site = '클래스톡'
    try:
        likes = element.select_one('.product_star').text.split()[0]
    except:
        likes = ''
    
    onetime.append({
        "site" : site,
        "title" : element.select_one('h2').text,
        "category_2" : element.select_one('span').text.split(' · ')[0],
        "teacher" : element.select_one('span').text.split(' · ')[1],
        "s_price" : element.select_one('.price_info').text.split('\n')[1],
        "discount" : element.select_one('.price_info').text.split('\n')[2].replace(' 할인',''),
        "contentment" : likes,
        "link" : 'https://www.classtok.net' + element.get('href'),
    })
classtok_df = classtok_df.append(onetime)

print('time: ', round((time.time() - start)/60, 1), '분', sep='')
print('\n')



classtok_df.to_csv(f'/home/ubuntu/notebooks/crawl-repo-6/classtok_{datetime.datetime.now().strftime("%y%m%d%H%M%S")}.csv', encoding='utf-8')


print('전체')
print('time: ', round((time.time() - start)/60, 1), '분', sep='')
print('\n')
print('total: ', len(classtok_df), sep='')


