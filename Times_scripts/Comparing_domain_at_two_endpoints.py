#!/usr/bin/env python3

import requests
import os


class check_domain:
    def __init__(self, domain_name, uri):
        self.domain_name = domain_name
        self.uri = uri

    def domain_response_at_customeIP(self, VIP):
        self.VIP = VIP


    def domain_response_default_dns(self):


if __name__ == '__main__':
    domain = input("Please pass a Domain:\t")
    new_vip = input("Please pass a custom VIP to compare domain response:\t")
    API = input("Please pass specific API path or enter for default:\t")
    if API == '':
        API = '/'
    elif re.search('^/', API):
        pass
    else:
        print("Wrong API, please check, it should bw start from /")
        sys.exit(1)


