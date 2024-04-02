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