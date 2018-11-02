# coding=utf8

from datetime import datetime
import smtplib
from email.message import EmailMessage
#import os
from pathlib import Path
import sys
from configparser import ConfigParser

#config_path = os.path.join(os.path.dirname("~/.config/"), ".reminder")
config_path = "".join(str(Path.home()),".config/python-reminder")
print (config_path)

today = datetime.strftime(datetime.today(), "%d.%m")
print ("Today is", today)
def get_tasks():
    f = open("list.markdown","r")
    tasks = list()
    for row in f:
        if row[0:5]==today:
            tasks.append(row)
    return tasks
print (get_tasks())

host = "smtp"
subject = "Your personal reminder for %s" % today
address = "user"
sender = "sender_mail"
text = "Python 3.7 rules them all!"

body = "\r\n".join((
    "From: %s" % sender,
    "To: %s" % address,
    "Subject: %s" % subject ,
    "",
    text
))

#server = smtplib.SMTP(host)
#server.connect(host,587)
#server.ehlo()
#server.starttls()
#server.ehlo()
#server.login(login, password)
#server.sendmail(sender, [address], body)
#server.quit()
