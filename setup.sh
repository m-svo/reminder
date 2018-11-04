#!/bin/bash

cp config-template config
cp list-template.markdown list.markdown
echo "WARNING! This software stores your email login and password in plain text in home folder. Please, do not use an important email account."
chmod +x reminder.py
echo "Would you like a simlink to list.markdown in HOME? Y/N"
read symlink
if [[ $symlink == "Y" ]] || [[ $symlink == "y" ]]
then
  echo "Making symlink"
  ln -s link.markdown ~/link.markdown
fi
echo "Input SMTP server:"
read smtp_server
echo "Input SMTP port:"
read smtp_port
echo "Input your sending email:"
read smtp_sender
echo "Input email login:"
read smtp_login
echo "Input email password:"
read smtp_password
echo "Input target email (where you will get notifications):"
read target_email
sed -i -e 's/smtp.example.com/'"$smtp_server"'/' config
sed -i -e 's/587/'"$smtp_port"'/' config
sed -i -e 's/example@email.com/'"$smtp_sender"'/' config
sed -i -e 's/example-to@email.com/'"$target_email"'/' config
sed -i -e 's/example-login@mail.com/'"$smtp_login"'/' config
sed -i -e 's/examplepassword/'"$smtp_password"'/' config
echo "You may be prompted for sudo password to set up logging to /var/log/python_reminder"
sudo mkdir /var/log/python_reminder
sudo touch /var/log/python_reminder/log
echo "Setup finished. You should set up cronjob for 'reminder.py'."
