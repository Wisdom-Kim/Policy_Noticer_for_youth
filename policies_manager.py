from selenium import webdriver
from user import User
from feed import Feed
from selenium.webdriver.common.by import By
import time

def get_last_index(url):
    #TODO 해당 함수를 '괄호 안 요소를 추출하는 함수'로 범용화시키기
    driver.get(url)
    fn = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]").get_attribute("onclick")
    
    def find_index():
        #함수 매개변자를 찾아 인덱스를 반환하는 함수
        first_index = fn.find('(')
        last_index=fn.find(')')
        return fn[first_index+1:last_index]
    
    return find_index()

def find_id(feed):
    feed.find_element(By.CLASS_NAME,"item").get_attribute("onclick")

def create_feed(content):
    content = feed.find_element(By.CLASS_NAME,"content")
    try:
        state= content.find_element(By.CLASS_NAME,"state").text
        if(state=='모집중'):
            category= content.find_element(By.CLASS_NAME,"cate").text
            title= content.find_element(By.CLASS_NAME,"name").text
            src = feed.find_element(By.TAG_NAME,"img").get_attribute("src")
            #TODO 피드의 ID 추출하기
            #Feed(title,category,src,fid)
    except Exception as e:
        # 모집 중이 아닌 기업은 pass
        pass

driver = webdriver.Chrome()
BASE_URL = 'https://youth.seoul.go.kr'
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'
#user=User(None,)
driver.get(URL)
feeds = driver.find_elements(By.CLASS_NAME,"feed-item")




for feed in feeds:
    content = feed.find_element(By.CLASS_NAME,"content")
    try:
        state= content.find_element(By.CLASS_NAME,"state").text
        if(state=='모집중'):
            category= content.find_element(By.CLASS_NAME,"cate").text
            title= content.find_element(By.CLASS_NAME,"name").text
            src = feed.find_element(By.TAG_NAME,"img").get_attribute("src")
            
    except Exception as e:
        # 모집 중이 아닌 기업은 pass
        pass
    
#print(feeds)
#TODO 함수 리팩토링
last_index = get_last_index(URL)

time.sleep(1000)