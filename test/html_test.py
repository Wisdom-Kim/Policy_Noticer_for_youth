from test_html import HTML
from test_policy import Policy_feed

test_policy = Policy_feed(fid='1735987')
test_policy._thumbnail_url='https://youth.seoul.go.kr/atch/getImg.do?atchFileSn=1725482&ordr=1'
test_policy._category='문화'
test_policy._title='테스트지롱!'

test_policy2 = Policy_feed(fid='51453')
test_policy2._thumbnail_url='https://youth.seoul.go.kr/atch/getImg.do?atchFileSn=1724577&ordr=1'
test_policy2._category='주거'
test_policy2._title='테슽흐!'

policy_list=[{'123123':test_policy},{'13534515':test_policy2}]

source = HTML() #init_code 자동 생성
source.insert_content(policy_list)
source.finish_code()
with open('test1.html','w',encoding='utf8') as f:
    f.write(source._html)