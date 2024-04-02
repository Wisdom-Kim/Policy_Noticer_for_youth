from policy import Policy_feed
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time


#########################전처리#################################
def pretreatment_db(file) ->list:
    try:
        with open(file,'r') as f:
            return [fid.strip('\n') for fid in f.readlines()]
    except Exception:
        print("파일이 없는데요??")

def remove_bracket(component) ->str:
    #괄호 안 요소를 반환
    first_index = component.find('(')
    last_index=component.find(')')
    return component[first_index+1:last_index].strip('\'')

def get_page_component(component) -> str:
    # 크롤링한 피드 컴포넌트의 속성 중 마지막 페이지가 속한 부분을 반환
    return component.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]').get_attribute("onclick")

def get_fid_component(item) -> str:
    # 크롤링한 피드 컴포넌트의 속성 중 피드의 id가 속한 부분을 반환
    return item.find_element(By.CLASS_NAME,"item-overlay").get_attribute("onclick")

#########################정책생성#############################
def create_policy(feed) -> object:
    #크롤링된 컴포넌트 내 정보를 기반으로 객체 생성후 반환
    content = feed.find_element(By.CLASS_NAME,"content")
    state = feed.find_element(By.CLASS_NAME,"state")
    if(state!='마감'):
        category= feed.find_element(By.CLASS_NAME,"cate").text
        title= content.find_element(By.CLASS_NAME,"name").text
        src = feed.find_element(By.TAG_NAME,"img").get_attribute("src")
        fid = remove_bracket(get_fid_component(feed))
    return Policy_feed(title,category,src,fid)

def write_db(file,id) -> None:
    #database.txt에 파일 내용저장
    #딕셔너리에 존재하지 않는 id만 db에 추가하므로, write_db 이후에 save_policies를 호출할 것
    with open(file,'a') as f: f.write(f'{id}\n')

##################################################################

def filter_init(**kwargs) -> None:
    #카테고리, 대상 기반 필터링
    pass
    
#TODO filter_init, crawling_init 완성
def crawling_init(driver,URL) -> None:
    driver.get(URL)
    #filter_init()
    #필터별로 선택
    
    #모집 중 필터
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/a').click()
    time.sleep(1)
    #모집중
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/div/ul/li[2]').click()
    #검색버튼 클릭
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[3]/button').click()
    time.sleep(1)

def get_last_page(driver):
    last_index = int(remove_bracket(get_page_component(driver)))
    return last_index
    
    #last index만큼 '>'를 누르면서 DB에 저장
    
def next_page(driver, cur_page):
    #현재 페이지에서 다음페이지로 이동
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR,f"a[onclick^={cur_page+1}]")
        driver.execute_script("arguments[0].click();", next_btn)
    except Exception:
        print("마지막이네!")

def save_new_policy(driver,database) -> dict:

    policy_dict ={} # id : 객체

    while(True):
        #마지막 인덱스로 갈 때까지 저장하면서 페이지 넘기기
        next_btn = driver.find_element(By.NAME,'a.arr1.next')
        last_index = int(remove_bracket(get_page_component(driver)))
        feeds = driver.find_elements(By.CLASS_NAME,"feed-item")
        
        for feed in feeds:
            try:
                fid = remove_bracket(get_fid_component(feed))
                if(fid not in database):
                    #객체 생성
                    policy = create_policy(feed)
                    #database.txt에 fid저장
                    write_db(database, policy.get_fid())
                    policy_dict[policy.get_fid()]=policy
            except NoSuchElementException:
                #상태 태그가 존재하지 않음
                print("태그 정보 없음")
                
        time.sleep(1)
        #다음 버튼 클릭
        if idx==last_index:
           break

    return policy_dict