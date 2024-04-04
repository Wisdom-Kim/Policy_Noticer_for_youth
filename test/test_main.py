from test_interface import *
from test_mail import *
from test_crawling_manager import *
from test_filter import *

# cm = Crawling_Manager()
app = UI()
# app.print_menu()
# app.input_target()
# app.input_area()
#메뉴 입력받기
ft = Filter(ward=1,area=2,target=1)
cm = Crawling_Manager()
cm.crawling_init(ft)
database = cm.pretreatment_db('database.txt')
policy_dict = cm.save_new_policy(database)
email = app.input_email()
#메일링을 위한 서버 구동
server = Server()
msg = write_msg(server,policy_dict,email)
server.send_email(msg)