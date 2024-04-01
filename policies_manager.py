from selenium import webdriver
from user import User
from feed import Feed
from selenium.webdriver.common.by import By
import time

def get_page_component(component) -> str:
    # 피드 컴포넌트의 속성 중 마지막 페이지가 속한 부분을 반환
    fn = component.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]').get_attribute("onclick")
    return fn

def get_fid_component(item) -> str:
    # 피드 컴포넌트의 속성 중 피드의 id가 속한 부분을 반환
    return item.find_element(By.CLASS_NAME,"item-overlay").get_attribute("onclick")

def remove_bracket(component) ->str:
    first_index = component.find('(')
    last_index=component.find(')')
    return component[first_index+1:last_index].strip('\'')

def create_policy(feed) -> object:
    #컴포넌트 내 정보를 기반으로 객체 생성
    content = feed.find_element(By.CLASS_NAME,"content")
    try:
        state= content.find_element(By.CLASS_NAME,"state").text
        if(state=='모집중'):
            category= feed.find_element(By.CLASS_NAME,"cate").text
            title= content.find_element(By.CLASS_NAME,"name").text
            src = feed.find_element(By.TAG_NAME,"img").get_attribute("src")
            fid = remove_bracket(get_fid_component(feed))
            return Feed(title,category,src,fid)
    except Exception as e:
        # 모집 중이 아닌 기업은 pass
        pass

def write_id(id) -> None:
    with open('database.txt','a') as f:
        f.write(id+"\n")

driver = webdriver.Chrome()
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

base = driver.get(URL)

feeds = driver.find_elements(By.CLASS_NAME,"feed-item")
recruit_filter_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/a').click()
time.sleep(1)
search_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/div/ul/li[2]').click()
time.sleep(1)

policy_list =[]
for feed in feeds:
    policy_list.append(create_policy(feed))
    fid = remove_bracket(get_fid_component(feed))
    write_id(fid)

print(policy_list)
#print(feeds)
last_index = remove_bracket(get_page_component(driver))
time.sleep(1000)