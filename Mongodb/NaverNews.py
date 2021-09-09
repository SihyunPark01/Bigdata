"""
날짜 : 2021/08/31
이름 : 박시현
내용 :  파이썬 가상브라우저 뉴스 크롤링 실습
"""

import time
from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 뉴스 이동 - IT/일반 의 모든 뉴스를 다 파싱할 것임
browser.get('https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230')


i, page = 0, 1
j = 0

while True:

    # 수집하는 페이지 날짜 출력

    viewday = ''
    span_viewday = browser.find_element_by_css_selector('#main_content > div.pagenavi_day > span.viewday')
    viewday = span_viewday.text

    if viewday == '12월31일':
        break


    print('%s 수집시작'% viewday)



    while True:
        try:
            # 뉴스 목록 가져오기
            tags_a = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:not(.photo) > a') #ul 2개 X li 6개

            for index, tag in enumerate(tags_a):
                pass
                #print('{}\t{}\t{}'.format(index, tag.text, tag.get_attribute('href')))

            # 다음 페이지 클릭
            pages_a = browser.find_elements_by_css_selector('#main_content > div.paging > a')
            pages_a[i].click() #2페이지
            print('%d 페이지 완료...'% page)

            i += 1
            page += 1

            if page % 10 == 1: #page그룹의 첫번째 페이지 일때
                i = 1


        except:
            print('%s 데이터 수집 끝...'% viewday)
            page = 1
            i = 0

            # 전일로 이동
            pages_day = browser.find_elements_by_css_selector('#main_content > div.pagenavi_day > a')
            pages_day[j].click() # 0,1,2,2,2,2,2,2,,,,,,이런 패턴이 성립.

            if j < 2:
                j += 1

            break

# 브라우저 종료
browser.quit()