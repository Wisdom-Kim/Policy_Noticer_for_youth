from old_interface import *
from mail import *
from crawling_manager import *
from custom_filter import *

# cm = Crawling_Manager()
# app.menu()
#메뉴 입력받기
cm = Crawling_Manager()
cm.crawling_init(app.my_filter)
database = cm.pretreatment_db('database.txt')
policy_dict = cm.save_new_policy(database)
email = app.input_email()
#메일링을 위한 서버 구동
server = Server()
msg = write_msg(server,policy_dict,email)
server.send_email(msg)