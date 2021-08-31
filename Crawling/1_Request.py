"""
날짜 : 2021/08/30
이름 : 박시현
내용 :  파이썬 HTML 페이지 요청하기 실습
"""

import requests as req

url = 'https://www.naver.com/'

# 페이지 요청하기
html = req.get(url).text
print(html)
