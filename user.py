class User:
    def __init__(self):
        self.__password =None
        self.__email = None
    
    @property
    def _password(self):
        return self.__password

    @_password.setter
    def _password(self, value):
        self.__password = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

