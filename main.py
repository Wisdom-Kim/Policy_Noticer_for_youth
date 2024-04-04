from old_interface import *
from mail import *
from crawling_manager import *
from custom_filter import *

app = UI()
app.print_menu()
app.input_target()

#조건에 맞게 크롤링
cm = Crawling_Manager()
cm.crawling_init(app.my_filter)
database = cm.pretreatment_db('database.txt')
policy_list = cm.save_new_policy(database)

email = app.input_email()      
        
#메일링을 위한 서버 구동
server = Server()

source = HTML() #init_code 자동 생성
source.insert_content(policy_list)
source.finish_code()

msg = server.write_msg(source._html,email)
server.send_email(msg)
