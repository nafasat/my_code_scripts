#!/usr/bin/env python3

import re


def check_files(input_file):
    file = open(input_file, 'r')

    regex = '''(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

    InActive_nodes = []
    Active_nodes = []

    for i in file:
        if re.search(r'drain', i):
            for matches in re.finditer(regex, i):
                InActive_nodes.append(i[matches.start():matches.end()])
        else:
            for matches in re.finditer(regex, i):
                Active_nodes.append(i[matches.start():matches.end()])

    print("|  Active_Nodes   |  Passive_Nodes  |")
    if len(Active_nodes) > len(InActive_nodes):
        max_len: int = len(Active_nodes)
        for index in range(max_len - len(InActive_nodes)):
            Active_nodes.append("NA")
    else:
        max_len: int = len(InActive_nodes)
        for index in range(max_len - len(Active_nodes)):
            Active_nodes.append("NA")

    for item in range(max_len):
        print("| %-15s | %-15s |" % (Active_nodes[item], InActive_nodes[item]))

    file.close()


for i in ['/tmp/123', '/tmp/123SSL']:
    check_files(i)
    print("------------------------------------")
