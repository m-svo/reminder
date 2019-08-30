#!/usr/bin/env python3
# coding=utf8

from datetime import datetime
import smtplib
from email.message import EmailMessage
from pathlib import Path
from configparser import ConfigParser

join_paths = (str(Path(__file__).parent),"/config")
join_paths_list = (str(Path(__file__).parent),"/list.markdown")
config_path = "".join(join_paths)
list_path = "".join(join_paths_list)
config = ConfigParser()
config.read(config_path)

today = datetime.strftime(datetime.today(), "%d.%m")
day = datetime.strftime(datetime.today(), "%d")
weekday = "day "+str(datetime.today().isoweekday())

def get_tasks():
    f = open(list_path,"r")
    tasks = list()
    for row in f:
        if row[0:5]==today:
            tasks.append(row) # append onetime and yearly tasks
        if row[0:5]==day+".XX":
            tasks.append(row) # append monthly tasks
        if row[0:5]==weekday:
            tasks.append(row) # append weekly tasks
    return tasks
get_tasks()

date_now = datetime.now()


if get_tasks():
    log_text = "Tasks sent."
    host = config.get("smtp", "server")
    port = config.get("smtp", "port")
    subject = "Your personal reminder for %s" % today
    address = config.get("smtp", "to")
    sender = config.get("smtp", "from")
    text = "".join(get_tasks())

    body = "\n".join((
        "From: %s" % sender,
        "To: %s" % address,
        "Subject: %s" % subject ,
        "",
        text
    ))

    server = smtplib.SMTP(host)
    server.connect(host,port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.get("smtp","login"),config.get("smtp","password"))
    server.sendmail(sender, [address], body.encode("utf-8"))
    server.quit()
else:
    log_text = "No tasks found."

log=open("/var/log/python_reminder/log","a")
log.write("Reminder executed on %s. %s \n" % (date_now,log_text))
