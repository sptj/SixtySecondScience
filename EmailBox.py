# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class EmailBox:
    def __init__(self,text_body="default"):
        self.sender = 'xinyuecai_kindle@163.com'
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        self.receivers = ['xinyuecai@kindle.com']
        # 设置eamil信息
        # 添加一个MIMEmultipart类，处理正文及附件
        self.message = MIMEMultipart()
        self.message['From'] = self.sender
        self.message['To'] = self.receivers[0]
        self.message['Subject'] = 'convert'
        msg = MIMEText(text_body, 'html', 'utf-8')
        self.message.attach(msg)
    def add_attachment(self,file_name,file_content):
        attachment = MIMEText(file_content, 'html', 'utf-8')
        # 附件设置内容类型，方便起见，设置为二进制流
        attachment['Content-Type'] = 'application/octet-stream'
        # 设置附件头，添加文件名
        attachment['Content-Disposition'] = 'attachment;filename="%s.html"'%file_name
        # 将内容附加到邮件主体中
        self.message.attach(attachment)
    def send_email(self):
        #登录并发送
        try:
            # 设置服务器所需信息
            # 163邮箱服务器地址
            mail_host = 'smtp.163.com'
            # 163用户名
            mail_user = 'xinyuecai_kindle'
            # 密码(部分邮箱为授权码)
            mail_pass = ''
            # 邮件发送方邮箱地址
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host,25)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(
                self.sender,self.receivers,self.message.as_string())
            print('success')
            smtpObj.quit()
        except smtplib.SMTPException as e:
            print('error',e)
if  __name__=="__main__":
    t=EmailBox("sertvsrtvaerasdfaerfdsztrrfasdfsdtdvxd")# Alien langue, ignore it
    t.send_email()