#!/usr/bin/env python3
# coding=utf8

import sys
from pathlib import Path

join_paths_list = (str(Path(__file__).parent),"/list.markdown")
list_path = "".join(join_paths_list)

args = ("weekly","monthly","onetime","yearly")
start = 0
end = 0

def print_usage():
    print ("""
        Incorrect call.

        Arguments:
        weekly - prints weekly tasks
        monthly - prints monthly tasks
        onetime - prints onetime tasks
        yearly - prints yearly tasks""")
    return "Incorrect call"

def check_args(arg,tasks_list):
    global start,end
    if arg in sys.argv and len(sys.argv) == 2:
        try:
            start = tasks_list.index("### " + arg + "\n") + 1
            end = tasks_list.index("### /" + arg + "\n")
            return True
        except:
            return None

def get_tasks():
    f = open(list_path,"r")
    tasks = list()
    for row in f:
        tasks.append(row)
    if len(sys.argv) == 2:
        if sys.argv[1] in args:
            check_args(sys.argv[1],tasks)
            selected_tasks = tasks[start:end]
            for x in selected_tasks:
                sys.stdout.write(x)
            return selected_tasks
        else:
            return print_usage()
    else:
        return print_usage()

# no need to call get_tasks() because the next check calls it as part of check
if not get_tasks():
    print ("Could not find any of requested tasks.")
