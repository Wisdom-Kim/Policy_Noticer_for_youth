#######터미널을 이용한 input
from test_filter import Filter
#정규표현식을 위한 re import
import re

class UI:
    def __init__(self):
        self.my_filter= Filter()
    
    def decorate(func):
        def print_deco(self):
            print("=" * 60)
            func(self)
            print("=" * 60)
        return print_deco
    
    @decorate    
    def print_menu(self):
        print('\t\t해당되는 항목을 골라주세요\n')
        for idx, keyword in enumerate(self.my_filter.target_list):
            print('\t\t' + f'{idx+1} {keyword}')
    
    @decorate 
    def input_target(self):
        #인덱스이기 때문에 -1
        target=''
        target_list=[]
        reg = '^[1-8]$'
        while(re.compile(reg).match(target) is None):
            target = input("해당하는 번호를 알려주세요! >>> ")

        target=int(target)-1
        target_list.append(target)
        self.my_filter._target=target_list
            
    @decorate
    def input_email(self) -> str:
        user_mail =''
        reg = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while(re.compile(reg).match(user_mail) is None):
            user_mail = input('소식을 받을 메일 주소를 입력해주세요!: ')
            
        return user_mail
    
    @decorate
    def input_area(self) ->list:
        #direction은 지역 인덱스
        #wards.index(user_input)은 자치구 인덱스
        while True:  # 무한 반복
            area_idx=0
            user_input = input("자치구 이름을 입력하세요: ")
            for areas in self.my_filter.ward_list.values(): #([종로구,중구...].[도봉구,성동구....],....)
                area_idx+=1
                if user_input in areas:
                    #print(f"{user_input}은(는) {area_idx}에 위치하며, 리스트 내 인덱스는 {areas.index(user_input)}입니다.")
                    self.my_filter._area=area_idx
                    
                    return [area_idx,areas.index(user_input)]
            print(f"잘못된 입력입니다. 서울에 있는 자치구를 입력해주세요!")

# 인스턴스 생성 및 메소드 호출
    
app=UI()
app.print_menu()
app.input_target()
app.input_area()