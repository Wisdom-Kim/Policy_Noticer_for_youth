class Policy_feed():
    def __init__(self,title,category,thumbnail_url,fid):
        self.__title = title
        self.__category=category
        self.__thumbnail_url= thumbnail_url
        self.__fid = fid

    @property
    def _title(self):
        return self.__title

    @_title.setter
    def _title(self, value):
        self.__title = value

    @property
    def _category(self):
        return self.__category

    @_category.setter
    def _category(self, value):
        self.__category = value

    @property
    def _thumbnail_url(self):
        return self.__thumbnail_url

    @_thumbnail_url.setter
    def _thumbnail_url(self, value):
        self.__thumbnail_url = value

    @property
    def _fid(self):
        return self.__fid

    @_fid.setter
    def _fid(self, value):
        self.__fid = value
        
    
