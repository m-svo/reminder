#!/usr/bin/env python3

import sys
from pathlib import Path

# Join needs a tuple
list_path = "".join( ( str(Path(__file__).parent), "/list.markdown" ) )

args = ("onetime", "weekly", "monthly", "yearly")
start = 0
end = 0

def print_usage():
    """Prints usage."""
    print ("""
        Incorrect call.

        Arguments:
        onetime - prints onetime tasks
        weekly - prints weekly tasks
        monthly - prints monthly tasks
        yearly - prints yearly tasks""")
    return "Incorrect call"

def check_args(arg, tasks_list):
    """Return position for an argument.

    Takes an argument(str) and a list,
    gets start and end positions for this argument.
    """
    global start, end
    try:
        start = tasks_list.index("### " + arg + "\n") + 1
        end = tasks_list.index("### /" + arg + "\n")
        return True
    except ValueError:
        return None

def get_tasks():
    """Get tasks by position.

    Write result to stdout, also return result.
    Call print_usage() when wrong or no argument provided.
    """
    with open(list_path, "r") as f:
        tasks = list()
        for row in f:
            tasks.append(row)
        if len(sys.argv) == 2:
            if sys.argv[1] in args:
                check_args(sys.argv[1], tasks)
                selected_tasks = tasks[start:end]
                for x in selected_tasks:
                    sys.stdout.write(x)
                return selected_tasks
            else:
                return print_usage()
        else:
            return print_usage()

# No need to explicitly call get_tasks() because next check calls it.
if not get_tasks():
    print ("Could not find any of requested tasks.")
