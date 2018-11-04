# reminder  
Email reminder in Python to execute as cron job  
This is a small personal project, so may not work for everyone.  
`reminder.py` reads tasks from `list.markdown` by `date.month` only, so it is best used for recurring reminders, like birthdays, taxes, etc.  
If there are tasks for today, email is generated and sent.  
Regardless of the above, log is written to `/var/log/python_reminder/log` every time `reminder.py` has executed successfully.  

# prerequisites  
- Python 3  
- being okay with some email account login and password being stored in plaintext in $HOME  

# warning  
This software stores your email login and password in plain text in home folder. Please, do not use an important email account.  

# installation  
```
git clone https://github.com/m-svo/reminder.git
cd reminders
chmod +x setup.sh
./setup.sh
```
- do not forget to setup a cron job. `reminder.py` can be executed directly, no need to specify `python3` executable if Python 3 is correctly installed.
