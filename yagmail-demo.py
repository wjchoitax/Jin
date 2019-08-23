# import yagmail
#
# yag = yagmail.SMTP(user='wjchoitax', password='dnrwls2#')
# yag.send('cheri50@naver.com', 'yagmail test', 'content...')
# print('send ok..')

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = smtplib.SMTP(host='smtp.naver.com', port=587)
smtp.ehlo()
smtp.starttls()
smtp.login(user='cheri50', password='chldnrwls1!')

msg = MIMEText('본문입니다.')
msg['Subject'] = Header('제목입니다', charset='utf-8')
msg['From'] = 'cheri50@naver.com'
msg['To'] = 'wjchoitax@gmail.com'


smtp.send_message(msg)

smtp.quit()

