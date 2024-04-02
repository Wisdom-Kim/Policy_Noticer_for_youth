
#  클래스
#import os

from selenium import webdriver

# [추가]
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://youth.seoul.go.kr/mainA.do")

# Policy 클래스는 데이터를 크롤링하여 정제 및 가공하는 역할
class Policy_feed():
    def __init__(self,title,category,thumbnail_url,fid):
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
    def __init__ (self, title, category, thumbnail_url, fid):
        #super().__init__(title, category, thumbnail_url, fid)
        #신청기간
        self.__applc_period = None
        #진행일정
        self.__schedule = None
        #담당기관
        self.__agency = None
        #참여인원
        self.__join_people = None
        #신청대상
        self.__subject_applc = None
        #지원내용
        self.__sup_contents = None
        #참여비
        self.__entry_fee = None
        #신청방법
        self.__applc_method = None
        #상세 이미지 주소 리스트
        self.__img_url = []

    """ get을 사용하여 가독성 정리하기..?? """
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

def fetch_data(self):
    try:
  
        for i in range(len(titles)):
            policy = Policy(titles[i].text, categories[i].text, thumbnail_urls[i], fids[i])
            driver.get("https://youth.seoul.go.kr/infoData/sprtInfo/view.do?sprtInfoId=" + policy.get_fid())
            
            # 텍스트 분할을 통한 정보 수집
            table_rows = driver.find_elements(By.CSS_SELECTOR, ".editor-text")
            for row in table_rows:
                row_text = row.text
                if '신청 기간' in row_text:
                    policy.applc_period = row_text.split('editor-text')[1].strip()
                elif '진행일정' in row_text:
                    policy.schedule = row_text.split('editor-text')[1].strip()
                elif '담당기관' in row_text:
                    policy.agency = row_text.split('editor-text')[1].strip()
                elif '참여인원' in row_text:
                    policy.join_people = row_text.split('editor-text')[1].strip()
                elif '신청대상' in row_text:
                    policy.subject_applc = row_text.split('editor-text')[1].strip()
                elif '지원내용' in row_text:
                    policy.sup_contents = row_text.split('editor-text')[1].strip()
                elif '참여비' in row_text:
                    policy.entry_fee = row_text.split('editor-text')[1].strip()
                elif '신청방법' in row_text:
                    policy.applc_method = row_text.split('editor-text')[1].strip()
                
                # 상세 이미지 주소
                image_elements = driver.find_elements(By.CSS_SELECTOR, ".policy_detail img")
                policy.img_url = [image.get_attribute("src") for image in image_elements]
                
    except Exception as e:
        self.handle_exception(e)
    
    finally:
        driver.quit()

