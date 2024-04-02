from policy import Policy_feed
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

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

def write_db(policy_dict,id) -> None:
    #database.txt에 파일 내용저장
    #딕셔너리에 존재하지 않는 id만 db에 추가하므로, write_db 이후에 save_policies를 호출할 것
    try:
        with open('database.txt','a') as f:
            if(policy_dict.get(id)==None):
                #딕셔너리에 id 정보가 존재하지 않는다면, db에 쓴다.
                f.write(f'{id}\n')
    except Exception:
        #파일이 없어서 에러가 났다면 새로 쓰기
         with open('database.txt','w') as f:
             f.write(f'{id}\n')

# def is_exist(driver,class_name) -> bool:
#     try:
#         driver.find_element(By.CLASS_NAME,class_name)
#     except NoSuchElementException:
#         print("야아ㅓㅏㅣ너아ㅣㅁ러아ㅣㄹ")
#         return False
#     return True
    
##############################################################################

def filter_init(**kwargs) -> None:
    #카테고리, 대상 기반 필터링
    pass
    

def crawling_init(driver, URL) -> None:
    driver.get(URL)
    
    #모집 중 필터
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/div/ul/li[2]').click()
    time.sleep(1)
    
    #카테고리, 대상 입력 받은 후 filter_init()
    
    #last index만큼 '>'를 누르면서 DB에 저장
def dic_init(driver) -> dict:
    last_index = int(remove_bracket(get_page_component(driver)))
    policy_dict ={} # id : 객체
    
    for _ in range(last_index):
        feeds = driver.find_elements(By.CLASS_NAME,"feed-item")
        for feed in feeds:
            try:
                if(feed.find_element(By.CLASS_NAME,"state")!='마감'):
                    policy = create_policy(feed)
                    write_db(policy_dict, policy.get_fid())
                    policy_dict[policy.get_fid()]=policy
            except NoSuchElementException:
                print("정보 없음")
                
        driver.find_element(By.CLASS_NAME,'next').click()

    return policy_dict