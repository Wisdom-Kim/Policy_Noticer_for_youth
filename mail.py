import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
##
from py_html import HTML
from policy import Policy_feed
##
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
                   
    def write_msg(self,source,email)-> object: # content 반환
        
        msg =  MIMEMultipart('alternative')
        msg['Subject']='짜잔!🥰 요청하신 정책 정보입니다!'
        msg.attach(MIMEText(source, 'html', _charset='UTF-8'))
        msg['From'] = self._SMTP_USER
        msg['To'] = email
        return msg

'''
실사용은 어떻게?

source = HTML() #init_code 자동 생성
source.insert_content(policy_list)
source.finish_code()
server.write_msg(server,source._html,email)
'''