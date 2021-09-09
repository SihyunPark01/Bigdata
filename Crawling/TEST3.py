
from selenium import webdriver
from datetime import datetime
import pandas as pd

#가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

#기상청 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

i = 0
for i in range(95):
    # 지역 클릭
    area = browser.find_elements_by_css_selector('#weather_table > tbody > tr')
    area[i].click()
    # print(len(area))
    print(area[i].text)

    # 파일 생성
    result = pd.DataFrame(area)
    result.to_csv('./Weather_%Y-%m-%d-%H-%M.csv'.format(datetime.now()), index=False, encoding='cp949')



