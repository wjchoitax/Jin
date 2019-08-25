import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


LOGIN_ID = 'wjchoi@ecredible.co.kr'
LOGIN_PW = ''

driver = webdriver.Chrome('./chromedriver')
driver.get('https://webfax.uplus.co.kr/main')

time.sleep(2)

driver.find_element_by_id('loginId').send_keys(LOGIN_ID)
time.sleep(1.5)

driver.find_element_by_id('loginPwd').send_keys(LOGIN_PW)
time.sleep(1.5)
driver.find_element_by_id('loginPwd').send_keys(Keys.RETURN)
# driver.find_element_by_id('loginBtn').click()

time.sleep(3)

driver.find_element_by_id('recvInfo').click()

# 웹페이지의 소스를 가져옴. ajax 요청 대응도 가능함.
html = driver.page_source

time.sleep(5)

driver.close()
