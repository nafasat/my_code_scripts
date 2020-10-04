#!/usr/bin/env python3

import sys
import re
import requests
from colored import fg, bg, attr, stylize
import colored

print("%sVIP\tBackEnd_Nodes_List%s" % (fg(34), attr(0)))
angry = colored.fg("red") + colored.attr("bold")
light_angry = colored.fg("magenta") + colored.attr("bold")

def get_details(VIP):
    Query = "https://cmdbapi.timesinternet.in/api/v0.1/vipmembermapping?vip=" + VIP
    Result = requests.get(Query).json()["data"]
    if not Result:
        print(stylize("%-10s\t[VIP_with_0_nodes]" % VIP, light_angry))
    else:
        print("%-10s\t%-10s" % (VIP, Result))


def check(input_ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    if re.search(regex, input_ip):
        get_details(input_ip)
    else:
        print(stylize("%-10s\t[Invalid_VIP]" % input_ip, angry))


if __name__ == '__main__':
    try:
        check(sys.argv[1])
    except Exception:
        try:
            File = open('/tmp/VIP.txt', 'r')
        except Exception:
            print("Input File Error")
            sys.exit(1)
        for input_ip in File:
            check(input_ip.strip())
