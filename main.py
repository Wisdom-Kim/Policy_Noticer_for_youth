from selenium import webdriver
from crawling_manager import *

driver = webdriver.Chrome()
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

database = pretreatment_db('database.txt')
crawling_init(driver,URL)
policy_dict = save_new_policy(driver,database)
time.sleep(100)
