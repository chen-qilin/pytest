#!/usr/bin/env python
# coding = utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = 'chen_qilin@163.com'
receiver = 'chen_qilin@163.com'
subject = 'python email test'
username = 'chen_qilin'
password = '***'

msg = MIMEText('Hello World', 'plain')
msg['Subject'] = Header(subject)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
