#!/usr/bin/env python3

import requests
from requests_toolbelt.adapters import host_header_ssl
from prettytable import PrettyTable
import os
import re
import sys


class check_domain_status:
    def __init__(self, domain_name, uri):
        self.uri = uri
        self.domain_name = domain_name

    def check_dns_record(self):
        Query = 'dig +short ' + self.domain_name + ' @8.8.8.8'
        if ''.join(os.popen(Query).readlines()) == '':
            return False
        else:
            return True

    def http_check(self):
        URL = 'http://' + self.domain_name + self.uri
        try:
            return requests.get(URL, timeout=5).status_code
        except requests.ConnectTimeout:
            return "TimeOut_Error"
        except requests.ConnectionError:
            return "Connection_Error"

    def https_check(self):
        try:
            URL_HTTPS = 'https://' + self.domain_name + self.uri
            return requests.get(URL_HTTPS, timeout=5).status_code
        except requests.ConnectTimeout:
            return "TimeOut_Error"
        except requests.ConnectionError:
            return "Connection_Error"

    def ssl_url_check_custom_IP(self, node_ip):
        self.node_ip = node_ip
        https_url_ip = 'https://' + self.node_ip + self.uri
        s = requests.Session()
        s.mount('https://', host_header_ssl.HostHeaderSSLAdapter())
        try:
            rhttps = s.get(https_url_ip, headers={"Host": self.domain_name}, timeout=5)
            return rhttps.status_code
        except requests.ConnectTimeout:
            return "TimeOut_Error"
        except requests.ConnectionError:
            return "Connection_Error"

    def url_check_custom_IP(self, node_ip):
        self.node_ip = node_ip
        http_url_ip = 'http://' + self.node_ip + self.uri
        try:
            r = requests.get(http_url_ip, headers={'host': self.domain_name}, timeout=5)
            return r.status_code
        except requests.ConnectionError:
            return "Connection_Error"
        except requests.ConnectTimeout:
            return "TimeOut_Error"


if __name__ == '__main__':
    AD = input("Please pass Akamai Domain or just enter for ignore:\t")
    OD = input("Please pass Origin Domain or just enter for ignore:\t")
    API = input("Please pass specific API path or enter for default:\t")
    ND = input("Do you want to check origin domain at backend nodes (Y/N):\t").lower()
    result = {}
    if API == '':
        API = '/'
    elif re.search('^/', API):
        pass
    else:
        print("Wrong API, please check, it should bw start from /")
        sys.exit(1)
    x = PrettyTable()
    x.field_names = ['Domain_Name', 'HTTP_Response', 'HTTPS_Response']
    if AD != '':
        ad = check_domain_status(AD, API)
        if not ad.check_dns_record():
            print("Failed")
        else:
            result[AD] = {}
            x.add_row([AD, ad.http_check(), ad.https_check()])

    if OD != '':
        od = check_domain_status(OD, API)
        if not od.check_dns_record():
            print("Failed")
        else:
            result[OD] = {}
            x.add_row([OD, od.http_check(), od.https_check()])
    if AD == '' and OD == '':
        print("Pass at least a domain")
        sys.exit(1)
    print("\n", x.get_string())

    if ( ND == 'y' or ND == 'yes' ) and OD != '':
        IP = ''.join(os.popen('dig +short ' + OD + ' @8.8.8.8').readlines()).strip()
        if not IP == '':
            y = PrettyTable()
            y.field_names = ['Node_IP', 'HTTP_Response', 'HTTPS_Response']
            Query = "https://cmdbapi.timesinternet.in/api/v0.1/vipmembermapping?vip=" + IP
            Result = requests.get(Query).json()["data"]
            for nodeIP in Result:
                y.add_row([nodeIP, od.url_check_custom_IP(nodeIP), od.ssl_url_check_custom_IP(nodeIP)])
            print("\nResult for domain %s at Node ip" % OD)
            print(y.get_string())
