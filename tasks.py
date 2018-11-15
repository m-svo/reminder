#!/usr/bin/env python3
# coding=utf8

import sys
from pathlib import Path

join_paths_list = (str(Path(__file__).parent),"/list.markdown")
list_path = "".join(join_paths_list)

def get_tasks():
    f = open(list_path,"r")
    tasks = list()
    for row in f:
        tasks.append(row)
    start = 0
    end = 0
    if 'monthly' in sys.argv and len(sys.argv) == 2:
        start = tasks.index('### monthly\n') + 1
        end = tasks.index('### /monthly\n')
    if 'onetime' in sys.argv and len(sys.argv) == 2:
        start = tasks.index('### onetime\n') + 1
        end = tasks.index('### /onetime\n')
    if 'yearly' in sys.argv and len(sys.argv) == 2:
        start = tasks.index('### yearly\n') + 1
        end = tasks.index('### /yearly\n')
    selected_tasks = tasks[start:end]
    for x in selected_tasks:
        sys.stdout.write(x)
    return selected_tasks

# no need to call get_tasks() because the next check calls it as part of check
if not get_tasks():
    print ("Could not find any of requested tasks.")

def print_usage():
    print ("""
    Incorrect call.
    
    Arguments:
    monthly - prints monthly tasks
    onetime - prints onetime tasks
    yearly - prints yearly tasks""")

if not 'onetime' in sys.argv and not 'monthly' in sys.argv and not 'yearly' in sys.argv or len(sys.argv) != 2:
    print_usage()
