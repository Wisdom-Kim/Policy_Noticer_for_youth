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

# def get_page_component(component) -> str:
#     # 크롤링한 피드 컴포넌트의 속성 중 마지막 페이지가 속한 부분을 반환
#     return component.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]').get_attribute("onclick")

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

def write_db(file_name,id) -> None:
    #database.txt에 파일 내용저장
    #딕셔너리에 존재하지 않는 id만 db에 추가하므로, write_db 이후에 save_policies를 호출할 것
    with open(file_name,'a') as f: f.write(f'{id}\n')

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
    search_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[3]/button')

    driver.execute_script("arguments[0].click();", search_btn)
    time.sleep(1)

def get_last_page(driver):
    last_index = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]').get_attribute("onclick")
    last_index = int(remove_bracket(last_index))
    return last_index
    
    #last index만큼 '>'를 누르면서 DB에 저장
    
def next_page(driver, cur_page) -> int:
    #현재 페이지에서 다음페이지로 이동
    try:
        function_name = 'fn_egov_link_page'
        xpath = f"//a[contains(@onclick, '{function_name}({cur_page+1})')]"
        next_btn = driver.find_element(By.XPATH, xpath)
        
        driver.execute_script("arguments[0].click();", next_btn)
        return int(cur_page)+1
    except Exception as e:
        print(e)

def save_new_policy(driver,database) -> dict:

    policy_dict ={} # id : 객체
    cur_idx =1
    
    last_index = get_last_page(driver)
    while(last_index > cur_idx):
        #마지막 인덱스로 갈 때까지 저장하면서 페이지 넘기기
        
        feeds = driver.find_elements(By.CLASS_NAME,"feed-item")
        for feed in feeds:
            try:
                fid = remove_bracket(get_fid_component(feed))
                if(fid not in database):
                    #database에 db가 없다면 객체 생성 후 txt에 fid기입
                    policy = create_policy(feed)
                    write_db('database.txt', policy._fid)
                    
                    policy_dict[policy._fid]=policy
                    
            except NoSuchElementException:
                #상태 태그가 존재하지 않음
                print("상태 정보 없음")
                
        cur_idx = next_page(driver,cur_idx)

    return policy_dict