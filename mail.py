import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

from policy import Policy_feed

load_dotenv()

class Server:
    def __init__(self):
        self.SMTP_SERVER='smtp.gmail.com'
        self.SMTP_PORT = 587
        self.__SMTP_USER = os.getenv('SMTP_USER')
        self.__PASSWORD = os.getenv('SMTP_PASSWORD')
     
    @property
    def _SEND_USER(self):
        return self.__SEND_USER

    @_SEND_USER.setter
    def _SEND_USER(self, value):
        self.__SEND_USER = value
          
    @property
    def _SMTP_USER(self):
        return self.__SMTP_USER

    @_SMTP_USER.setter
    def _SMTP_USER(self, email):
        self.__SMTP_USER = email

    @property
    def _PASSWORD(self):
        return self.__PASSWORD

    @_PASSWORD.setter
    def _PASSWORD(self, password):
        self.__PASSWORD = password
    
    def send_email(self,msg):
        
        smtp = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self._SMTP_USER, self._PASSWORD)
        smtp.sendmail(self._SMTP_USER,msg['To'], msg.as_string())
        smtp.quit()
        return smtp
                
#메세지 텍스트 작성
#매개로 받는 딕셔너리는{id:객체(title, category가 프로퍼티)}의 집합
def dict_to_content(dictionary) ->str:
    content = ""
    for new_policy in dictionary.values():
        content += "="*30 + "\n"
        content += f"제목 : {new_policy._title}\n"
        content += "="*30 + "\n"
        #content += 이미지
        content += f"카테고리 : {new_policy._category}\n"
    return content        
        
def write_msg(server,policy_dict,email)-> object: # content 반환
    text= dict_to_content(policy_dict)
    msg =  MIMEMultipart('alternative')
    msg['Subject']='짜잔!🥰 요청하신 정책 정보입니다!'
    msg.attach(MIMEText(text, 'plain', _charset='UTF-8'))
    msg['From'] = server._SMTP_USER
    msg['To'] = email
    return msg