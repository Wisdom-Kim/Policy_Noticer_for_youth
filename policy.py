
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
class Policy(Policy_feed):
    def __init__ (self, title, category, thumbnail_url, fid):
        super().__init__(title, category, thumbnail_url, fid)
        #신청기간
        self.applc_period = None
        #진행일정
        self.schedule = None
        #담당기관
        self.agency = None
        #참여인원
        self.join_people = None
        #신청대상
        self.subject_applc = None
        #지원내용
        self.sup_contents = None
        #참여비
        self.entry_fee = None
        #신청방법
        self.applc_method = None
        #상세 이미지 주소 리스트
        self.img_url = []
            
    # 수집한 데이터를 가공하여 반환
    def process_data(self, data):
        processed_data = []
        for policy in data:
            processed_data.append
            ({
                "title": policy.get_title(),
                "category": policy.get_category(),
                "thumbnail_url": policy.get_thumbnail(),
                "fid": policy.get_fid(),
                "applc_period": policy.applc_period,
                "schedule": policy.schedule,
                "agency": policy.agency,
                "join_people": policy.join_people,
                "subject_applc": policy.subject_applc,
                "sup_contents": policy.sup_contents,
                "entry_fee": policy.entry_fee,
                "applc_method": policy.applc_method,
                "img_url": policy.img_url
            })
        return processed_data
    
    # 예외 처리
    def handle_exception(self, e):
        print(f"예외 발생: {e}")

    # 파일 저장 코드 작성??
    def save_to_file(self, data, filename):
        pass
    
    
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
                    policy.schedule = row_text.split('진행')[1].strip()
                elif '담당기관' in row_text:
                    policy.agency = row_text.split('담당기관')[1].strip()
                elif '참여인원' in row_text:
                    policy.join_people = row_text.split('참여인원')[1].strip()
                elif '신청대상' in row_text:
                    policy.subject_applc = row_text.split('신청대상')[1].strip()
                elif '지원내용' in row_text:
                    policy.sup_contents = row_text.split('지원내용')[1].strip()
                elif '참여비' in row_text:
                    policy.entry_fee = row_text.split('참여비')[1].strip()
                elif '신청방법' in row_text:
                    policy.applc_method = row_text.split('신청방법')[1].strip()
                
                # 상세 이미지 주소
                image_elements = driver.find_elements(By.CSS_SELECTOR, ".policy_detail img")
                policy.img_url = [image.get_attribute("src") for image in image_elements]
                
    except Exception as e:
        self.handle_exception(e)
    
    finally:
        driver.quit()