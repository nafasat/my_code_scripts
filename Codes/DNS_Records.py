#!/usr/bin/python3
# from typing import TextIO

import dns.resolver
import os


Domains = ['www.magicbricks.com', 'www.google.com']

print('Domain\tRecord_Name\tResult')


def check_records(dom, record):
    try:
        result = dns.resolver.resolve(dom, record)
        for data in result:
            print(dom,'\t',record,'\t',data)
    except Exception as e:
        print(dom,'\t',record,'\t','NoAnswer')


for domain in Domains:
    for i in ['A','CNAME','MX']:
        check_records(domain, i)