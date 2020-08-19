import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project  # 'dbsparta'라는 이름의 db를 만듭니다

headers = {
    'User-Agent': '# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

#######i4p 브랜드 가져오기######

##ndcip category##

for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/ndcip/79/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)

            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 ndcip category입니다######')

##top category##
for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/top/68/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)
            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 top category입니다######')

##bottom category##
for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/bottom/26/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)
            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 bottom category입니다######')


##acc category##
for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/acc/27/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)
            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 acc category입니다######')


##eyewear category##
for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/eyewear/70/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)
            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 eyewear category입니다######')

##custom category##
for page in range(1, 5):  # 그냥 첫 페이지부터 끝까지 안되는지 물어보기
    print('page ', page)
    url = 'http://i4p.kr/category/custom/56/?page={}'.format(page)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    item_details = soup.find_all('li', attrs = {'id' : re.compile('^anchorBoxId_')})
    for detail in item_details:

        name = detail.select_one('div.description > span.name > a > span:nth-child(2)')
        price = detail.select_one('div.description > ul > li > span:nth-child(2)')
        img_url = detail.select_one('div.thumbnail > a > img')['src']
        sold_out = detail.find('img', attrs = {'alt' : '품절'})
        if not sold_out:  # 품절 제품 제외
            if img_url.startswith('//') :
                img_url = 'http:' + img_url
                print(name.text, price.text, img_url)
            doc = {
                'name': name.text,
                'price' : price.text,
                'img_url': img_url
            }

            db.i4p.insert_one(doc)
print('#####여기까지가 custom category입니다######')