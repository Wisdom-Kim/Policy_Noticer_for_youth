#import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://youth.seoul.go.kr/infoData/sprtInfo/view.do?sprtInfoId=51538&key=2309130006&pageIndex=1&orderBy=regYmd+desc&recordCountPerPage=8&sc_ctgry=&sw=&viewType=on&sc_aplyPrdEndYmdUseYn=&cntrLa=37.566761128870546&cntrLo=126.97862963872868&neLat=37.566761128870546&neLng=126.97862963872868&swLat=37.566761128870546&swLng=126.97862963872868&mapLvl=6&sarea=")

# Policy 클래스는 데이터를 크롤링하여 정제 및 가공하는 역할
class Policy_feed():
    def __init__(self, title, category, thumbnail_url, fid):
        self.__title = title
        self.__category=category
        self.__thumbnail_url= thumbnail_url
        self.__fid = fid
        
    def get_title(self):
        return self.__title
    
    def get_category(self):
        return self.__category
    
    def get_thumbnail(self):
        return self.__thumbnail_url
    
    def get_fid(self):
        return self.__fid

# 자식
class Policy():
    def __init__ (self, applc_period, schedule, agency, join_people,subject_applc,sup_contents, entry_fee, applc_method,img_url):
        #super().__init__(title, category, thumbnail_url, fid)

        #신청기간
        self.__applc_period = applc_period
        #진행일정
        self.__schedule = schedule
        #담당기관
        self.__agency = agency
        #참여인원
        self.__join_people = join_people
        #신청대상
        self.__subject_applc = subject_applc
        #지원내용
        self.__sup_contents = sup_contents
        #참여비
        self.__entry_fee = entry_fee
        #신청방법
        self.__applc_method = applc_method
        #상세 이미지 주소 리스트
        self.__img_url = img_url

    """ get """
    # Getter메서드
    def get_applc_period(self):
        return self.__applc_period
    
    def get_schedule(self):
        return self.__schedule

    def get_agency(self):
        return self.__agency

    def get_join_people(self):
        return self.__join_people

    def get_subject_applc(self):
        return self.__subject_applc

    def get_sup_contents(self):
        return self.__sup_contents

    def get_entry_fee(self):
        return self.__entry_fee

    def get_applc_method(self):
        return self.__applc_method

    def get_img_url(self):
        return self.__img_url

# 텍스트 전처리 함수
def need_info(text):
    return text.strip()

def fetch_data(self):
    try:
        # 텍스트 분할을 통한 정보 수집
        row_text  = driver.find_element(By.CLASS_NAME, "editor-text").text
        print(row_text)
        if '신청 기간' in row_text:
           period = row_text.split('editor-text')[1].strip()
           print(period)
        if '진행일정' in row_text:
            schedule = row_text.split('editor-text')[1].strip()
            print(schedule)
        if '담당기관' in row_text:
            agency = row_text.split('editor-text')[1].strip()
            print(agency)
        if '참여인원' in row_text:
            join_people = row_text.split('editor-text')[1].strip() 
            print(join_people) 
        if '신청대상' in row_text:
            subject_applc = row_text.split('editor-text')[1].strip()
            print(subject_applc)
        if '지원내용' in row_text:
            sup_contents = row_text.split('editor-text')[1].strip()
            print(sup_contents)
        if '참여비' in row_text:
            entry_fee = row_text.split('editor-text')[1].strip()
            print(entry_fee)
        if '신청방법' in row_text:
            applc_method = row_text.split('editor-text')[1].strip()
            print(applc_method)
            
            # 상세 이미지 주소
            image_elements = driver.find_elements(By.CSS_SELECTOR, ".policy_detail img")
            img_url = [image.get_attribute("src") for image in image_elements]
            
            # Policy 인스턴스 생성 및 반환
            policy_instance = Policy(period, schedule, agency, join_people, subject_applc, sup_contents, entry_fee, applc_method, img_url)
            
            return policy_instance
            
    except Exception as e:
        print(e)
        #policy_instance.handle_exception(e)
    
    finally:
        driver.quit()

fetch_data(driver)

# # Selenium 설정
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# Policy 객체 생성 및 데이터 수집
# policy_instance = Policy("Sample Title", "Sample Category", "Sample Thumbnail URL", "Sample FID")

# 데이터 수집 및 출력

# 수집한 데이터에 접근
#print(policy_instance.get_title())
#print(policy_instance.get_applc_period())
