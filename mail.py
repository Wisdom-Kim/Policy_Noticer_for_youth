from selenium import webdriver
from crawling_manager import *
###############################
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

class Server:
    def __init__(self):
        self.SMTP_SERVER='smtp.gmail.com'
        self.SMTP_PORT = 587
        self.__SEND_USER=''
        self.__SMTP_USER = os.environ.get('SMTP_USER')
        self.__PASSWORD = os.environ.get('SMTP_PASSWORD')
     
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
        
        self._SEND_USER= input('메일을 받을 이메일 주소를 입력해주세요!: ')
        
        try:
            with smtplib.SMTP(self.SMTP_SERVER,self.SMTP_PORT) as server:
                server.starttls()
                server.login(self._SMTP_USER,self._PASSWORD)
                server.sendmail(self._SMTP_USER, msg['To'], msg.as_string())   
        
        except Exception as e:
            print(e)
        
#메세지 텍스트 작성

#딕셔너리는{id:객체(title, category가 프로퍼티)}의 집합
def dict_to_content(dictionary) ->str:
    content = ""
    for new_policy in dictionary.values():
        content += "="*30 + "\n"
        content += f"제목 : {new_policy._title}\n"
        content += "="*30 + "\n"
        #content += 이미지
        content += f"내용 : {new_policy._category}\n"
    return content        
        
def write_msg(server,policy_dict)-> object: # content 반환
    text= dict_to_content(policy_dict)
    msg =  MIMEMultipart('mixed')
    msg['Subject']='짜잔!🥰 요청하신 정책 정보입니다!'
    msg.attach(MIMEText(text, 'plain', _charset='UTF-8'))
    msg['From'] = server._SMTP_USER
    msg['To'] = server._SMTP_USER
    return msg
    


##############
    
#driver = webdriver.Chrome()
#URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

#database = pretreatment_db('database.txt')
#crawling_init(driver,URL)
#policy_dict = save_new_policy(driver,database)#database에 없는 조건에 맞는 정책들이 담긴 딕셔너리

test = {'11111':Policy_feed('제목','카테고리','썸네일주소','11111')}
server = Server()
msg = write_msg(server,test)
server.send_email(msg)
# ###############
# time.sleep(100)