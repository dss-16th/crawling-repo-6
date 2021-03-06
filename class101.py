
# -*- coding: utf-8 -*-
import requests
import time
import datetime
import pandas as pd
start  = time.time()

offset = 28 * 0
limit = 28 * 38
url_graphql = 'https://cdn-gql-prod2.class101.net/graphql'

cat_ko_ls = ['취미', '수익창출', '직무교육']
cat_eng_ls = ['creative', 'money', 'career']
brands = ["original", "money", "professional"]
categories = list(zip(cat_ko_ls, cat_eng_ls, brands))

req = requests.get('https://class101.net/robots.txt')
prohibit_url = []
for txt in req.text.split('\n'):
    if 'Disallow: ' in txt:
        prohibit_url.append('https://class101.net' + txt.replace('Disallow: ', ''))
        

class101_df = pd.DataFrame(columns=['url_detail', 'url', 'title', 'category_1', 'category_2', 'state', 'o_price', 's_price', 'teacher', 'teacher_nick', 'feedback_count', 'feedback_good', 'reservation', 'heart'])

for cat_ko, cat_eng, brand in categories:
    print(f'{cat_ko} / {cat_eng}')
    query = [{"operationName":"InfiniteProductCardsWithLastUpdatedInformation","variables":{"brand":[brand],"offset":offset,"limit":limit},"query":"query InfiniteProductCardsWithLastUpdatedInformation($brand: [ProductBrand!], $limit: Int, $offset: Int, $categoryIds: [String!]) {\n  products(\n    limit: $limit\n    offset: $offset\n    productFilter: {brand: $brand, isHidden: false, isLastManagement: true, state: [funding, sales], type: \"klass\", categoryIds: $categoryIds}\n    sort: [{managedAt: -1}]\n  ) {\n    ...ProductCardWithLastUpdatedInformation\n    __typename\n  }\n  productsCount(\n    productFilter: {brand: $brand, categoryIds: $categoryIds, isHidden: false, isLastManagement: true, state: [funding, sales], type: \"klass\"}\n  )\n}\n\nfragment ProductCardWithLastUpdatedInformation on Product {\n  _id\n  categoryId\n  categoryIds\n  coverImageUrl\n  firestoreId\n  title\n  titlePrefixes\n  type\n  state\n  packagePricePreview {\n    listPrice\n    netPrice\n    __typename\n  }\n  ...CategoryAndCreatorTag\n  ...ProductBadge\n  ...LastUpdatedInformation\n  ...HeartAndFeedbackCountLabel\n  __typename\n}\n\nfragment CategoryAndCreatorTag on Product {\n  _id\n  category {\n    _id\n    title\n    __typename\n  }\n  categoryTitleDetail\n  difficulty\n  author {\n    _id\n    firestoreId\n    name\n    nickName\n    photoUrl\n    channels {\n      type\n      url\n      channelId\n      __typename\n    }\n    createdAt\n    __typename\n  }\n  __typename\n}\n\nfragment ProductBadge on Product {\n  productBadge {\n    text\n    imageUrl\n    backgroundColor\n    fontColor\n    __typename\n  }\n  __typename\n}\n\nfragment LastUpdatedInformation on Product {\n  _id\n  lastManagement {\n    managedAt\n    content\n    __typename\n  }\n  __typename\n}\n\nfragment HeartAndFeedbackCountLabel on Product {\n  _id\n  feedbackCount\n  feedbackGoodCount\n  reservationCount\n  wishlistedCount\n  __typename\n}\n"}]
    req = requests.post(url_graphql, json=query)
    datas = req.json()


    onetime = []
    for i in range(len(datas[0]['data']['products'])):
        url_detail = datas[0]['data']['products'][i]['_id']
        url = 'https://class101.net/products/' + url_detail
        if url in prohibit_url:
            continue
        title = datas[0]['data']['products'][i]['title']
        category_1 = cat_ko
        category_2 = datas[0]['data']['products'][i]['category']['title']
        state = datas[0]['data']['products'][i]['state']
        try:
            o_price = datas[0]['data']['products'][i]['packagePricePreview']['listPrice']
        except:
            o_price = '링크 참조'
            print('o_price', url, i)
        try:
            s_price = datas[0]['data']['products'][i]['packagePricePreview']['netPrice']
        except:
            s_price = '링크 참조'
            print('s_price', url, i)
        teacher = datas[0]['data']['products'][i]['author']['name']
        teacher_nick = datas[0]['data']['products'][i]['author']['nickName']
        feedback_count = datas[0]['data']['products'][i]['feedbackCount']
        feedback_good = datas[0]['data']['products'][i]['feedbackGoodCount']
        reservation = datas[0]['data']['products'][i]['reservationCount']
        heart = datas[0]['data']['products'][i]['wishlistedCount']


        row = {
            'url_detail': url_detail, 
            'url': url,
            'title': title, 
            'state': state, 
            'category_1': category_1,
            'category_2': category_2,
            'o_price': o_price, 
            's_price': s_price, 
            'teacher': teacher, 
            'teacher_nick': teacher_nick,
            'feedback_count': feedback_count, 
            'feedback_good': feedback_good, 
            'reservation': reservation, 
            'heart': heart
            }
        onetime.append(row)
        
        
    class101_df = class101_df.append(onetime)
    print('time: ', round((time.time() - start)/60, 1), '분', sep='')
    print('\n')

class101_df.to_csv(f'./datas/class101_{datetime.datetime.now().strftime("%y%m%d%H%M%S")}.csv', encoding='utf-8')


print('전체')
print('time: ', round((time.time() - start)/60, 1), '분', sep='')
print('\n')

print('total: ', len(class101_df), sep='')
for cat_ko in cat_ko_ls:
    print(f'{cat_ko}: ', len(class101_df[class101_df['category_1']==cat_ko]), sep='')

# url_detail, title, category_1, category_2, state, o_price, s_price, teacher, teacher_nick, feedback_count, feedback_good, reservation, heart
