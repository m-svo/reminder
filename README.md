# reminder  
Email reminder in Python to execute as cron job  
This is a small personal project, so may not work for everyone.  
`reminder.py` reads tasks from `list.markdown` by `date.month` or `date` only, so it is best used for recurring reminders, like birthdays, taxes, rent etc.  
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
cd reminder
chmod +x setup.sh
./setup.sh
```  
- do not forget to setup a cron job. `reminder.py` can be executed directly, no need to specify `python3` executable if Python 3 is correctly installed. Example:  
```
0 7 * * * <your-path-to-script>/reminder/reminder.py 1> /dev/null 2>> /var/log/python_reminder/log
```  
This will execute every day at 7:00 AM and append errors, if any, to `/var/log/python_reminder/log`
