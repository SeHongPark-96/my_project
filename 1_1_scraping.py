import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project  # 'dbsparta'라는 이름의 db를 만듭니다

headers = {
    'User-Agent': '# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

#######잔다리로 스토어 브랜드 가져오기######
for page in range(1, 5):
    print('page ', page)
    url = 'https://jandarirostore.com/418/?&page={}&sort=recent'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.select('#container_w202007276314e348892cc > div')
    for detail in item_details:

        name = detail.select_one('div.item-detail > div.item-pay > h2 > a')
        price = detail.select_one('div.item-detail > div.item-pay > div.item-pay-detail > p')
        img_url = detail.select_one('div.item-wrap > a > img._org_img.org_img._lazy_img')['src']
        sold_out = detail.select_one('div.item-detail > div.item-pay > div.ns-icon.clearfix > div')
        if not sold_out:  # 품절 제품 제외
            print(name.text, price.text, img_url)
            # doc = {
            #     'name': name.text,
            #     'price' : price.text,
            #     'img_url': img_url['src']
            # }
            #
            # db.jandariro.insert_one(doc)
