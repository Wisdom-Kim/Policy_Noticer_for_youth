from selenium import webdriver
from crawling_manager import *

driver = webdriver.Chrome()
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

crawling_init(driver,URL)
policy_dict = dic_init(driver)
time.sleep(100)