"""
날짜 : 2021/08/30
이름 : 박시현
내용 :  파이썬 parsing 실습

파싱(Parsing) - 마크업문서(반정형 데이터)에서 특정 태그의 데이터를 추출,처리하는 과정
"""

import requests as req

from bs4 import BeautifulSoup as bs

# 페이지 요청
url = 'https://news.naver.com/main/home.naver'
html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
#print(html)

# 페이지 파싱 (내가 원하는 정보만 추출)
dom = bs(html, 'html.parser')
titles = dom.select('#section_it > div.com_list > div > ul > li > a > strong')
#print(titles)

# 파싱데이터 출력
for tit in titles:
    print(tit.text) #print(tit.String)해도 됨. list배열의 <strong>태그를 뗀 내용만 출력하고 싶을 때.

# 다음 랭킹뉴스 1위~5위까지만 출력
url_daum = 'https://news.daum.net/ranking/popular'
html_daum = req.get(url_daum).text
# print(html_daum)

dom_daum = bs(html_daum, 'html.parser')
daum_titles = dom_daum.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

for i in range(5):
    print('%d위 : %s' % (i+1, daum_titles[i].text))



