from selenium import webdriver
from policy import Feed
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
    #괄호 안 요소를 반환
    first_index = component.find('(')
    last_index=component.find(')')
    return component[first_index+1:last_index].strip('\'')

def create_policy(feed) -> object:
    #컴포넌트 내 정보를 기반으로 객체 생성후 반환
    content = feed.find_element(By.CLASS_NAME,"content")
    try:
        state= content.find_element(By.CLASS_NAME,"state").text
        if(state=='모집중' or state == '상시'):
            category= feed.find_element(By.CLASS_NAME,"cate").text
            title= content.find_element(By.CLASS_NAME,"name").text
            src = feed.find_element(By.TAG_NAME,"img").get_attribute("src")
            fid = remove_bracket(get_fid_component(feed))
            return Feed(title,category,src,fid)
    except Exception as e:
        # 모집 중이 아닌 기업은 pass
        pass

def write_db(id) -> None:
    #database.txt에 파일 내용저장
    with open('database.txt','a') as f:
        f.write(id+"\n")

def save_policies(policy_feed) ->None:
    #딕셔너리에 {fid : policy_feed }저장
    policy_dict[policy_feed.fid]= policy_feed

driver = webdriver.Chrome()
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

base = driver.get(URL)

feeds = driver.find_elements(By.CLASS_NAME,"feed-item")
recruit_filter_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/a').click()
time.sleep(1)
search_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/div/ul/li[2]').click()
time.sleep(1)

policy_dict ={} # id : 객체

last_index = remove_bracket(get_page_component(driver))
time.sleep(1000)