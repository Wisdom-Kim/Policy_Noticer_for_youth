from test_html import HTML
from test_policy import Policy_feed

test_policy = Policy_feed()
test_policy._fid='123124'
test_policy._category='문화'
test_policy._thumbnail_url='https://youth.seoul.go.kr/atch/getImg.do?atchFileSn=1735987&ordr=1'
test_policy._title='테스트지롱!'

policy_list=[{'123123':test_policy}]

source = HTML() #init_code 자동 생성
source.insert_content(policy_list)
source.finish_code()
with open('test1.html','w',encoding='utf8') as f:
    f.write(source._html)