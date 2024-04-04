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

#email = app.input_email()      
#긴급한 에러 (app.input_email()이 반환이 되었다가 안되었다가 함!)
email =''
reg = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
while(re.compile(reg).match(email) is None):
    email = input('소식을 받을 메일 주소를 입력해주세요!: ')        

#메일링을 위한 서버 구동
server = Server()

source = HTML() #init_code 자동 생성
source.insert_content(policy_list)
source.finish_code()

msg = server.write_msg(source._html,email)
server.send_email(msg)
