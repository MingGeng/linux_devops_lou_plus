#!/usr/bin/python

import sys

if __name__ == '__main__':
    choose = 'tcp'
    if len(sys.argv) > 1:
        choose = sys.argv[1]
    main(choose)

PROC_FILE = {
    'tcp': '/proc/net/tcp',
    'tcp6': '/proc/net/tcp6',
    'udp': '/proc/net/udp',
    'udp6': '/proc/net/udp6'
}

def get_content(type):
    with open(PROC_FILE[type], 'r') as file:
        content = file.readlines()
        content.pop(0)
    return content

def main(choose):
    templ = "%-5s %-30s %-30s %-13s %-6s %s"
    print(templ % (
        "Proto", "Local address", "Remote address", "Status", "PID", "Program name"))
        content = get_content(choose)

