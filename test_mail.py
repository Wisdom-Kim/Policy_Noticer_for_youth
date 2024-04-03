from mail import *

'''
메세지 객체 작성 후 (msg는 MIMEMultipart를 이용해 생성)
아래 실행해주시면 됩니당
'''

server = Server()
server.send_email(msg)