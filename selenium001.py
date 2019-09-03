import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


LOGIN_ID = 'wjchoi@ecredible.co.kr'
LOGIN_PW = ''  # input("암호를 입력하세요: ")

driver = webdriver.Chrome('./chromedriver')
driver.get('https://webfax.uplus.co.kr/main')

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginId"))          # 웹브라우저가 활성화 될때까지 대기
    )
    driver.find_element_by_id('loginId').send_keys(LOGIN_ID)        # 로그인창에 ID 입력
    time.sleep(random.uniform(0.5, 2))
    driver.find_element_by_id('loginPwd').send_keys(LOGIN_PW)       # 로그인창에 PW 입력
    time.sleep(random.uniform(0.5, 2))
    driver.find_element_by_id('loginBtn').click()
    time.sleep(random.uniform(1, 2))

    driver.find_element_by_id('recvInfo').click()                   # 받은팩스함으로 이동
    time.sleep(random.uniform(0.5, 2))

    list_select = Select(driver.find_element_by_id('selectRpp'))
    list_select.select_by_visible_text('100')
    time.sleep(random.uniform(1, 2))
    # driver.find_element_by_id('sd').send_keys('20190901')           # 수신일 시작 입력
    # time.sleep(random.uniform(0.5, 2))
    # driver.find_element_by_id('sd').send_keys('20190903')           # 수신일 종료 입력
    # time.sleep(random.uniform(0.5, 2))
    #
    # driver.find_element_by_id('searchBtn').click()                   # 검색 버튼 선택

# driver.find_element_by_class_name('gnbSub_message').send_keys(Keys.RETURN)
# driver.find_element_by_id('loginPwd').send_keys(Keys.RETURN)

    html = driver.page_source                                           # 웹페이지의 소스를 가져옴. ajax 요청 대응도 가능함.
    origin_num_regex = re.compile('downloadImageBtn-\d{8}', re.VERBOSE)
    pattern_matched = origin_num_regex.findall(html)

    for i in pattern_matched:
        print(i)


finally:
    driver.close()
