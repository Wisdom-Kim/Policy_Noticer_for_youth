from interface import *
from mail import *
from crawling_manager import *
from custom_filter import *

cm = Crawling_Manager()
#app = UI(cm)
custom_filter = Filter()
#crawling_filter = app.apply_filter()
cm.crawling_init(custom_filter)
database = cm.pretreatment_db('database.txt')
policy_dict = cm.save_new_policy(database)
#email = app.input_email()

#메일링을 위한 서버 구동
# server = Server()
# msg = write_msg(server,policy_dict,email)
# server.send_email(msg)

