#!/usr/bin/env python3
import re
import requests
import sys


def get_domain_name(VIP):
    Query = "http://192.168.33.212:5000/api/v0.1/getdnsmapping?ip=" + VIP
    Result = requests.get(Query).json()["result"]
    if 'not found' in Result:
        print(VIP, "\tdomains_not_Mapped")
    else:
        List = Result[VIP]
        Alldomain = []
        for domains in List:
            Alldomain.append(''.join(domains.keys()))
        print(VIP, "\t", Alldomain)


def check(input_ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    if re.search(regex, input_ip):
        get_domain_name(input_ip)
    else:
        print(input_ip, "\t [Invalid_VIP]")


if __name__ == '__main__':
    try:
        check(sys.argv[1])
    except:
        try:
            File = open('/tmp/VIP.txt', 'r')
        except Exception:
            print("Input File Error")
            sys.exit(1)
        for input_ip in File:
            check(input_ip.strip())
