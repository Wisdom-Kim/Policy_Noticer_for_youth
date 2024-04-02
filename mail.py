from selenium import webdriver
from crawling_manager import *
###############################
from email.message import EmailMessage
import smtplib


def init_info(email, password):
    return {
        "smtp_server": smtplib.SMTP('smtp.gmail.com', 587),
        "smtp_port": 587,  # SMTP 서버 포트 설정
        "smtp_user_id": email,
        "smtp_user_pw": password,
    }

def write_msg_content(dictionary):
    msg = ""
    for new_policy in dictionary.values():
        msg += "="*30 + "\n"
        msg += f"제목 : {new_policy._title}\n"
        msg += "="*30 + "\n"
        msg += f"내용 : {new_policy._category}\n"
    return msg

def need_login(func):
    def wrapper(*args):

        my_email= input('메일을 받을 이메일 주소를 입력해주세요!: ')
        my_pwd= input('계정 비밀번호를 입력해주세요!')
        
        smtp_info = init_info(my_email,my_pwd)

        try:
            with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
                server.starttls() 
                server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
                result = func(*args) # write_email
                return result
        except Exception:
            print("로그인 과정에서 오류가 났습니다ㅠㅠ 다시 확인해주세요...")
            return -1
        
    return wrapper
        

def write_msg(smtp_info,policy_dict)-> object: # msg 반환
    msg = EmailMessage()
    msg['Subject']='짜잔!🥰 요청하신 정책 정보입니다!'
    msg.set_content(write_msg_content(policy_dict))
    msg['From'] = smtp_info["smtp_user_id"]
    msg['To'] = smtp_info["smtp_user_id"]
    return msg
    
@need_login
def send_email(smtp_info, policy_dict):
    msg = write_msg(smtp_info, policy_dict)
    smtp_info["smtp_server"].send_message(msg)

##############
    
driver = webdriver.Chrome()
URL = 'https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006'

database = pretreatment_db('database.txt')
crawling_init(driver,URL)
policy_dict = save_new_policy(driver,database)
send_email()
###############
time.sleep(100)