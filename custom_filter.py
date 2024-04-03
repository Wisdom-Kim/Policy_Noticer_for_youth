'''
카테고리, 대상

'''
class Filter:
    def __init__(self,cate=[],target=[]):
        self.__cate = cate
        self.__target = target

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
        
    def cate_list(self):
        return['전체','일자리','진로','창업','주거','금융','교육','마음건강','신체건강','생활지원','문화/예술','대외활동','공간','사회참여','커뮤니티']
    
    def target_list(self):
        return['제한없음','대학생','구직','재직','이직준비','시험준비','프리랜서','기타']
