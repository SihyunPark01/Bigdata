"""
날짜 : 2021/08/30
이름 : 박시현
내용 :  파이썬 날씨 데이터 크롤링 실습
"""
import requests as req
from bs4 import BeautifulSoup as bs
import os
from datetime import datetime


# 페이지 요청
url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
html = req.get(url).text
# print(html)

# 파싱하기
dom = bs(html, 'html.parser')
trs = dom.select('#weather_table > tbody > tr')

# 파일저장 디렉터리 생성 - 1시간마다 바뀐 데이터가 출력되도록!
directory = "./weather/{:%Y-%m-%d}".format(datetime.now())
if not os.path.exists(directory):
    os.makedirs(directory)

# 파일생성 - 1시간마다 바뀐 데이터가 출력되도록!
fname = "{:%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(directory+'/'+fname, 'w', encoding='utf-8')

for tr in trs:
    file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (tr.findChildren('td')[0].a.text,
                                                             tr.findChildren('td')[1].text,
                                                             tr.findChildren('td')[2].text,
                                                             tr.findChildren('td')[3].text,
                                                             tr.findChildren('td')[4].text,
                                                             tr.findChildren('td')[5].text,
                                                             tr.findChildren('td')[6].text,
                                                             tr.findChildren('td')[7].text,
                                                             tr.findChildren('td')[8].text,
                                                             tr.findChildren('td')[9].text,
                                                             tr.findChildren('td')[10].text,
                                                             tr.findChildren('td')[11].text,
                                                             tr.findChildren('td')[12].text))

file.close()
print('데이터 수집 완료...')