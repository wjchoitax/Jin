import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    driver.find_element_by_id('loginBtn').click()                   # 로그인 버튼 클릭
    time.sleep(random.uniform(1, 2))
    driver.find_element_by_id('recvInfo').click()                   # 받은팩스함으로 이동
    time.sleep(random.uniform(0.5, 2))

    # 출력날짜 설정
    driver.find_element_by_id('sd').click()                         # 수신 시작일 날짜선택 달력 팝업
    time.sleep(random.uniform(0.5, 2))
    day_picker: Select = Select(driver.find_elements_by_class_name('ui-state-default'))    # 수신 시작일 날짜선택 달력 팝업
    for i in day_picker:
        print(i)
    time.sleep(random.uniform(0.5, 2))
    driver.find_element_by_id('ed').click()                         # 수신 종료일 날짜선택 달력 팝업
    time.sleep(random.uniform(0.5, 2))

    # driver.find_element_by_id('searchBtn').click()                # 검색 버튼 선택

    # 발신번호 설정
    # list_select = Select(driver.find_element_by_id('selectRpp'))    # 목록 설정
    # list_select.select_by_visible_text('100')
    # time.sleep(random.uniform(1, 2))



# driver.find_element_by_class_name('gnbSub_message').send_keys(Keys.RETURN)
# driver.find_element_by_id('loginPwd').send_keys(Keys.RETURN)

    # html = driver.page_source                                           # 웹페이지의 소스를 가져옴. ajax 요청 대응도 가능함.
    # origin_num_regex = re.compile('downloadImageBtn-\d{8}', re.VERBOSE)
    # pattern_matched = origin_num_regex.findall(html)
    #
    # for i in pattern_matched:
    #     print(i)


finally:
    driver.close()
