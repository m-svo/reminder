#!/usr/bin/env bash

# get line number with string "synced from Nextcloud" in your list
# it MUST BE the last in your list.markdown
search_line=$(sed -n '/synced from Nextcloud/=' reminder/list.markdown)
# if the variable is not null
if [[ -n "$search_line" ]]
then
  # remove every line not in 1,search_line
  sed -i '1,'"$search_line"'!d' reminder/list.markdown
  # append reminder.txt from Nextcloud to your list
  cat /var/www/html/data/user/files/Documents/reminder.txt >> reminder/list.markdown
fi
