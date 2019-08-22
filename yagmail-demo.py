import yagmail

yag = yagmail.SMTP(user='wjchoitax', password='dnrwls2#')
yag.send('cheri50@naver.com', 'yagmail test', 'content...')
print('send ok..')