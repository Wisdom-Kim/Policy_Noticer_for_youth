# 파이썬 미니 프로젝트 (with 지혜님)
"""

[miniproject]

- 실습기간 : ~ 24.04.2~3(오전)(진행)
- 최소조건
	1. OOP
		1-1*) 함수, 클래스, 상속* 		
		1-2*) 실행 모듈(1개 : main.py)
			
	2. Skills
		2-1*) fetchData : crawling/API
		2-2*) file, exception, mail
		2-3) https://pyscript.net (옵션 -> 추후 적용해보기)

	3. Git
		3-1*) md
		3-2) issue, project(kanban)

- 실습순서
  1. 주제선정
crawling/OpenAPI : 사용할 수 있는 데이터 유무
  2. 설계
terminal 입력/출력
  3. 구현
    
    
"""

""" < 기능명세 >
    1-1) 유저에게 본인 정보를 입력 받는다.
    1-2) 현재 모집 현황이 ‘모집중’ ,’모집예정’,’상시’인 것을 대상으로 정보들을 검색한다.
          # 모집중    # <span class = "state bg-blue"> 모집중 </span>
          # 모집예정  # <span class = "state bg-purple"> 모집예정 </span>
          # 상시     #  <span class = "state bg-gray-e5"> 상시 </span>
    
    1-3) 검색 후 나오는 사이트들의 피드를 수집한다. 
    1-4) 피드 내 구조에 따라 메세지 객체를 생성한다.
    1-5) 메세지 객체를 생성 후 리스트에 담아둔다.

    2 개별 정책 소개 사이트를 대상으로 크롤링한다.
    
    3. 사이트 내 ‘신청 내용’ ,’신청 기간’ ‘활동내용’ 문구가 없다면, 예외처리를 이용해 이미지와 기본정보 (신청기간, 진행일정, 담당기관)만 함께 저장한다.
    
    4. 만약 문구가 있다면 '신청내용 / 신청기간 / 활동내용 / 활동시간' 등을 객체화시켜서 이미지와 함께 정리하여 객체 리스트에 담아준다.
    
    
    < 프로그램 구조 >
    1) 제목
    1-2) 카테고리
    1-3) 썸네일 이미지 주소()
    
    # editor-text
      # 텍스트는 텍스트로 추출하기
      
    1. 신청 기간
    2. 진행일정
    3. 담당기관

    (내용이 있다면)

    1. 참여인원
    2. 신청대상
    3. 지원내용
    4. 참여비
    5. 신청방법
    
    # img src
    6. 상세 이미지 주소 리스트
"""

# from policy import Policy

# def main():
#     pass
  
  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class Policy:
    def __init__ (self, applc_period, schedule, agency, join_people, subject_applc, sup_contents, entry_fee, applc_method, img_url):
        self.applc_period = applc_period
        self.schedule = schedule
        self.agency = agency
        self.join_people = join_people
        self.subject_applc = subject_applc
        self.sup_contents = sup_contents
        self.entry_fee = entry_fee
        self.applc_method = applc_method
        self.img_url = img_url

def fetch_data(driver):
    try:
        row_text = driver.find_element(By.CLASS_NAME, "editor-text").text

        applc_period = need_info('신청기간', row_text)
        schedule = need_info('진행일정', row_text)
        agency = need_info('담당기관', row_text)
        join_people = need_info('참여인원', row_text)
        subject_applc = need_info('신청대상', row_text)
        sup_contents = need_info('지원내용', row_text)
        entry_fee = need_info('참여비', row_text)
        applc_method = need_info('신청방법', row_text)

        image_elements = driver.find_elements(By.CSS_SELECTOR, ".policy_detail img")
        img_url = [image.get_attribute("src") for image in image_elements]

        return Policy(applc_period, schedule, agency, join_people, subject_applc, sup_contents, entry_fee, applc_method, img_url)
            
    except Exception as e:
        print(e)
        return None
    
    finally:
        driver.quit()

def need_info(keyword, text):
    lines = text.split('\n')
    
    for line in lines:
        if keyword in line:
            return line.split(':', 1)[1].strip()
    
    return ""

def main():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://youth.seoul.go.kr/infoData/sprtInfo/view.do?sprtInfoId=51538&key=2309130006&pageIndex=1&orderBy=regYmd+desc&recordCountPerPage=8&sc_ctgry=&sw=&viewType=on&sc_aplyPrdEndYmdUseYn=&cntrLa=37.566761128870546&cntrLo=126.97862963872868&neLat=37.566761128870546&neLng=126.97862963872868&swLat=37.566761128870546&swLng=126.97862963872868&mapLvl=6&sarea=")
    
    policy_data = fetch_data(driver)
    
    if policy_data:
        print("신청기간:", policy_data.applc_period)
        print("진행일정:", policy_data.schedule)
        print("담당기관:", policy_data.agency)
        print("참여인원:", policy_data.join_people)
        print("신청대상:", policy_data.subject_applc)
        print("지원내용:", policy_data.sup_contents)
        print("참여비:", policy_data.entry_fee)
        print("신청방법:", policy_data.applc_method)
        print("이미지 주소:", policy_data.img_url)
    
if __name__ == "__main__":
    main()