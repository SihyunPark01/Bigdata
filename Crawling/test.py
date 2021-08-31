
from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 싸이트로 이동
browser.get('https//www.naver.com')

