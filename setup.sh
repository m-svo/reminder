#!/bin/bash

mkdir $HOME/.config
cp .reminder_template $HOME/.config/python_reminder
cp list.markdown $HOME/list.markdown
echo "WARNING! This software stores your email password in plain text in home folder. Please, do not use an important email account."
echo "Input SMTP server:"
read smtp-server
echo "Input SMTP port:"
read smtp-port
echo "Input your sending email:"
read smtp-sender
echo "Input email login:"
read smtp-login
echo "Input email password:"
read smtp-password
echo "Input target email (where you will get notifications):"
read target-email
########### add write to $HOME/.config/python_reminder here
echo "You will be prompted for sudo password to set up logging to /var/log/python_reminder and cronjob"
sudo mkdir /var/log/python_reminder
sudo touch /var/log/python_reminder/log
