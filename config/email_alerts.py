import re
import pandas as pd
from email.mime.multipart import MIMEMultipart
import imp
import smtplib
import email.message
import glob

from email.mime.base  import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import os

def email_alerts(corpo):
   
    host='smtp.gmail.com'
    port='587'
    login='sintesebi.oem@gmail.com'
    senha='cdxxwlylmftqflrc' 

    server=smtplib.SMTP(host,port)

    server.ehlo()
    server.starttls()
    server.login(login,senha)
    recipients = ['saulo465@yahoo.com.br']
    email_msg=MIMEMultipart()
    email_msg['From']=login
    email_msg['To']= ", ".join(recipients)
    email_msg['Subject']='Alertas BOT'

    email_msg.attach(MIMEText(corpo, 'html'))
    i = 0
    server.sendmail(email_msg['From'],recipients, email_msg.as_string())
    server.quit()
# email_alerts('saulohssilva@gmail.com','saulo465@yahoo.com.br')
