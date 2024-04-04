from policy import Policy_feed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class Crawling_Manager:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'
        self.base_URL='https://youth.seoul.go.kr'

    ####################크롤링 데이터 전처리##########################
    def pretreatment_db(self,file) ->list:
        try:
            with open(file,'r') as f:
                return [fid.strip('\n') for fid in f.readlines()]
        except Exception:
            print("처음 실행해보셨군요!")
            with open(file,'w') as f:
                pass # 파일 만들기만 하기


    def remove_bracket(self,component) ->str:
        #괄호 안 요소를 반환
        first_index = component.find('(')
        last_index=component.find(')')
        return component[first_index+1:last_index].strip('\'')

    # def get_page_component(component) -> str:
    #     # 크롤링한 피드 컴포넌트의 속성 중 마지막 페이지가 속한 부분을 반환
    #     return component.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]').get_attribute("onclick")

    def get_fid_component(self,item) -> str:
        # 크롤링한 피드 컴포넌트의 속성 중 피드의 id가 속한 부분을 반환
        return item.find_element(By.CLASS_NAME,"item-overlay").get_attribute("onclick")

    ####################크롤링 데이터 정책생성#############################
    def create_policy(self,feed) -> object:
        #크롤링된 컴포넌트 내 정보를 기반으로 객체 생성후 반환
        content = feed.find_element(By.CLASS_NAME,"content")
        state = feed.find_element(By.CLASS_NAME,"state")
        if(state!='마감'):
            category= feed.find_element(By.CLASS_NAME,"cate").text
            title= content.find_element(By.CLASS_NAME,"name").text
            src = self.base_URL+feed.find_element(By.TAG_NAME,"img").get_attribute("src")
            fid = self.remove_bracket(self.get_fid_component(feed))
        return Policy_feed(title,category,src,fid)

    def write_db(self,file_name,id) -> None:
        #database.txt에 파일 내용저장
        #딕셔너리에 존재하지 않는 id만 db에 추가하므로, write_db 이후에 save_new_policy를 호출할 것
        with open(file_name,'a') as f: f.write(f'{id}\n')

    ##################################################################

    def filter_init(self, custom_filter) -> None:
        #필터 객체에 따라 카테고리 필터 요소 클릭

        #지역에 따라 조종
        if(custom_filter._area):
            
            area_filter_btn=self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[1]/a")
            #area_filter_btn.click()
            self.driver.execute_script("arguments[0].click();",area_filter_btn)
            time.sleep(1)

            xpath =f'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[1]/div/ul/li[{custom_filter._area}]/label' # 라벨
            self.driver.find_element(By.XPATH,xpath).click()

            # if(custom_filter._ward):
                
            #     ward_filter_btn=self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[2]/a")
            #     # ward_filter_btn.click()
            #     self.driver.execute_script("arguments[0].click();",ward_filter_btn)
            #     xpath=f'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[2]/div/ul/li[{custom_filter._ward}]/label' # 라벨
            #     self.driver.find_element(By.XPATH,xpath).click()
        
        if(custom_filter._target):
            target_filter_btn= self.driver.find_element(By.XPATH,f"/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[3]/a")#대상 버튼 클릭
            # target_filter_btn.click()
            self.driver.execute_script("arguments[0].click();",target_filter_btn)
            time.sleep(1)

            xpath=f'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[3]/div/ul/li[{custom_filter._target}]/label'#라벨
            self.driver.find_element(By.XPATH,xpath).click()

        
    def crawling_init(self,custom_filter) -> None:
        #filter 객체를 받아 filter init 실행 후, 조건에 맞도록 크롤링할 것
        self.driver.get(self.URL)
        self.filter_init(custom_filter)
        #필터별로 선택
        
        #모집 중 필터
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/a').click()
        time.sleep(1)
        #모집중
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[4]/ul/li[5]/div/ul/li[2]').click()
        #검색버튼 클릭
        search_btn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[3]/button')
        self.driver.execute_script("arguments[0].click();", search_btn)
        time.sleep(1)
        
        #왜인진 모르겠는데 사이트 자체에서 2번 클릭 되어야 제대로 필터링이 되어져서 나옴ㅠㅠ
        search_btn = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[2]/div[3]/button')
        self.driver.execute_script("arguments[0].click();", search_btn)


    def get_last_page(self)->int:
        #5개 이하일 때는 아래의 xpath 요소가 나타나지 않음
        try:
            xpath='/html/body/div[3]/div/div[1]/div/div[2]/form/div/div[4]/div[1]/div[2]/a[9]'
            last_index = self.driver.find_element(By.XPATH,xpath).get_attribute("onclick")
            last_index = int(self.remove_bracket(last_index))
            return last_index
        except Exception:
            return 5
        
        
        #last index만큼 '>'를 누르면서 DB에 저장
        
    def next_page(self, cur_page) -> int:
        #현재 페이지에서 다음페이지로 이동
        try:
            function_name = 'fn_egov_link_page'
            xpath = f"//a[contains(@onclick, '{function_name}({cur_page+1})')]"
            next_btn = self.driver.find_element(By.XPATH, xpath)
            
            self.driver.execute_script("arguments[0].click();", next_btn)
            return int(cur_page)+1
        except Exception:
            pass

    def save_new_policy(self,database) -> dict:

        policy_dict ={} # id : 객체
        cur_idx =1
        last_index = self.get_last_page() # 5페이지 이하일 경우 5로 임시 설정
        try:
            while(last_index > cur_idx):
                #마지막 인덱스로 갈 때까지 저장하면서 페이지 넘기기
                feeds = self.driver.find_elements(By.CLASS_NAME,"feed-item")
                for feed in feeds:
                    try:
                        fid = self.remove_bracket(self.get_fid_component(feed))
                        if(fid not in database):
                            #database에 db가 없다면 객체 생성 후 txt에 fid기입
                            policy = self.create_policy(feed)
                            self.write_db('database.txt', policy._fid)
                            
                            policy_dict[policy._fid]=policy
                            
                    except NoSuchElementException:
                        #상태 태그가 존재하지 않음
                        print("상태 정보 없음")     
                    cur_idx = self.next_page(cur_idx) #다음 페이지로 넘기기
        except Exception:
            print("끝까지 탐색했어요!")
        finally:
            return policy_dict