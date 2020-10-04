#!/usr/bin/env python3

import os
import re
from colored import fg, attr, stylize
import colored
import sys

print("%sVIP\tBackEnd_Nodes_List%s" % (fg(34), attr(0)))
angry = colored.fg("red") + colored.attr("bold")
light_angry = colored.fg("magenta") + colored.attr("bold")


def remote_copy(remote_ip, username, src_path, dest_path):
    command = 'scp -r ' + username + '@' + remote_ip + ':' + src_path + ' ' + dest_path
    print(command)
    return os.popen(command)


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


def check_vip(input_ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    if re.search(regex, input_ip):
        List_Nginx_Elb = ['172.29.145.252']
        HTTP_File = '/var/lib/nginx/state/backend*' + input_ip + '.conf'
        for elb in List_Nginx_Elb:
            dest_Path = '/tmp/' + elb + '/' + input_ip
            if not os.path.isdir(dest_Path):
                try:
                    os.makedirs(dest_Path)
                except OSError as error:
                    print(error)
            remote_copy(elb, 'nafasat.ahmed', HTTP_File, dest_Path)
            list_files = os.popen('ls -1 dest_Path')
    else:
        print(stylize("%-10s\t[Invalid_VIP]" % input_ip, angry))


if __name__ == '__main__':
    try:
        check_vip(sys.argv[1])
    except Exception:
        try:
            File = open('/tmp/VIP.txt', 'r')
            for input_ip in File:
                check_vip(input_ip.strip())
        except Exception:
            print("Input File Error")
            sys.exit(1)
