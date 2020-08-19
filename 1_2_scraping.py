import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project  # 'project'라는 이름의 db를 만듭니다

headers = {
    'User-Agent': '# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

#######선데이오프클럽 브랜드 가져오기######
url = 'https://sundayoffclub.com/product/list3.html?cate_no=102#'
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

item_details = soup.find_all('li', attrs={'id': re.compile('^anchorBoxId_')})

for detail in item_details:
    name = detail.select_one('div.box_wrap > a > center > span')
    price = detail.select_one('div.box_wrap > div.contents > ul > li > span')
    img_url = detail.select_one('div.box_wrap > div.img_box > a > img.big')['src']
    sold_out = detail.find('img', attrs = {'alt' : '품절'})

    if not sold_out :  # 품절 제품 제외
        if img_url.startswith('//'):
            img_url = 'http:' + img_url
            print(name.text, price.text, img_url)
        doc = {
            'name': name.text,
            'price': price.text,
            'img_url': img_url
        }

        db.sunday_off_club.insert_one(doc)


