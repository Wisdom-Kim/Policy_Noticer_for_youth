#######터미널을 이용한 input
from custom_filter import Filter
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
    def menu(self):
        print('\t\t해당되는 항목을 골라주세요')
        for idx, keyword in enumerate(self.my_filter.target_list):
            print('\t\t' + f'{idx+1} {keyword}')
    
    @decorate 
    def input_target(self):
        #인덱스이기 때문에 -1
        try:
            target_list=[]
            target = int(input("해당하는 번호를 알려주세요! >>> "))-1
            target_list.append(str(target))
            #TODO : 다중선택
            self.my_filter._target=target_list
        except Exception as e:
            print(e)
            print("1부터 8까지 번호 하나만 입력해주세요!")
            
    @decorate
    def input_email(self) -> str:
        user_mail =''
        reg = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while(re.compile(reg).match(user_mail) is None):
            user_mail = input('소식을 받을 메일 주소를 입력해주세요!: ')
            
        return user_mail             