#import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# 웹 드라이버 설정 및 웹 페이지 접속
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://youth.seoul.go.kr/infoData/sprtInfo/view.do?sprtInfoId=51421&key=2309130006&pageIndex=1&orderBy=regYmd+desc&recordCountPerPage=8&sc_ctgry=&sw=&viewType=on&sc_aplyPrdEndYmdUseYn=&cntrLa=37.566761128870546&cntrLo=126.97862963872868&neLat=37.566761128870546&neLng=126.97862963872868&swLat=37.566761128870546&swLng=126.97862963872868&mapLvl=6&sarea=")

# Policy 클래스는 데이터를 크롤링하여 정제 및 가공하는 역할
class Policy_feed:
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
class Policy:
    def __init__ (self, applc_period, schedule, agency, join_people,subject_applc,sup_contents, entry_fee, applc_method, img_url):
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



def need_info(keyword, text_list):
#한줄씪 키워드를 탐색 후, 원하는 정보를 반환하는 함수   
    start_idx = None
    end_idx = None
    
    for index, line in enumerate(text_list):
        
        if keyword in line:
            # start_idx = index + 1
            return text_list[index+1]
            
        # elif start_idx == '':
        #     end_idx = index
            
        #     break
    if start_idx == None:
        #찾지 못했으면
        return []
    # else:
    #     #찾았으면
    #     if(end_idx != None):
    #         #끝 줄을 찾았다면
    #         return text_list[start_idx:end_idx]
    #     else:
    #         return text_list[start_idx:]
    
    # if start_idx is not None and end_idx is not None:
    #     return text_list[start_idx:end_idx]
    
    # elif start_idx is not None:
    #     return text_list[start_idx: ]


def fetch_data(self):
    try:
        # 텍스트 분할을 통한 정보 수집
        row_text  = driver.find_element(By.CLASS_NAME, "editor-text").text.split('\n')

        # 전처리 함수를 이용하여 텍스트 정제
        if '신청기간' in row_text:
            applc_period = row_text.split('editor-text')[1].strip()
            print(applc_period)
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
            policy_instance = Policy(applc_period, schedule, agency, join_people, subject_applc, sup_contents, entry_fee, applc_method, img_url)
            
            return policy_instance
            
    except Exception as e:
        print(e)
    
    finally:
        driver.quit()

class Need_info:
    def __init__(self, info_list):
        self.period = info_list.get('기간', ''),
        self.schedule = info_list.get('일정', ''),
        self.agency = info_list.get('기관', ''),
        self.join_people = info_list.get('인원', ''),
        self.subject_applc = info_list.get('대상', ''),
        self.sup_contents = info_list.get('내용', ''),
        self.entry_fee = info_list.get('참여비', ''),
        self.applc_method = info_list.get('방법', ''),
        self.img_url = info_list.get('이미지', '')
        
        # self.period = period
        # self.schedule = schedule
        # self.agency = agency
        # self.join_people = join_people
        # self.subject_applc = subject_applc
        # self.sup_contents = sup_contents
        # self.entry_fee = entry_fee
        # self.applc_method = applc_method
        # self.img_url = img_url
        
    def __repr__(self):
        return f'기간 : {self.period}, 일정 : {self.schedule}'

def split_text(text):
    #text_list 반환
    return text.split('\n')


# 텍스트 데이터
text_data = driver.find_element(By.CLASS_NAME, "editor-text").text

print("=================================================")

#keywords = ['신청기간', '진행일정', '담당기관', '참여인원', '신청대상', '지원내용', '참여비', '신청방법']
keywords = ['기간', '일정', '기관', '인원', '대상', '내용' '참여비', '방법']

# 텍스트를 한 줄씩 쪼개서 리스트로 생성
text_lines = split_text(text_data)
# print(text_lines)
# 정보 추출
info_list = {}

for keyword in keywords:
    info = need_info(keyword, text_lines)
    if info:
    #info가 빈 리스트가 아니라면 아래 명령 실행
    #내용을 찾은 경우
        info_list[keyword] = info
# print(info_list)

# print(Need_info(info_list))

# 객체 생성
application_info = Need_info(info_list)
print(application_info)

# 정보 전달
policy = Policy(
    application_info.period,
    application_info.schedule,
    application_info.agency,
    application_info.join_people,
    application_info.subject_applc,
    application_info.sup_contents,
    application_info.entry_fee,
    application_info.applc_method,
    application_info.img_url,
    )
# print(policy)
