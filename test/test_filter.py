'''
카테고리, 대상

'''
class Filter:
    def __init__(self,cate=[],target=[],ward=[]):
        self.__cate = cate
        self.__target = target
        self.__ward = ward
        self.cate_list=['전체','일자리','진로','창업','주거','금융','교육','마음건강','신체건강','생활지원','문화/예술','대외활동','공간','사회참여','커뮤니티']
        self.target_list= ['제한없음','대학생','구직','재직','이직준비','시험준비','프리랜서','기타']
        #편의상 lsit라고 변수 명 지정
        self.ward_list = {
            '서북': ['종로구', '중구', '용산구', '은평구', '서대문구', '마포구'],
            '동북': ['도봉구', '성동구', '동대문구', '중랑구', '성북구', '강북구', '노원구'],
            '서남': ['양천구', '강서구', '구로구', '금천구', '영등포구', '관악구'],
            '동남': ['동작구', '광진구', '서초구', '강남구', '송파구', '강동구']
        }
    #TODO list메서드를 변수로 프로퍼티로 소환하기   
    @property
    def _ward(self):
        return self.__ward
    
    @_ward.setter

    @property
    def _cate(self):
        return self.__cate

    @_cate.setter
    def _cate(self, value):
        self.__cate = value

    @property
    def _target(self):
        return self.__target

    @_target.setter
    def _target(self, value):
        self.__target = value
