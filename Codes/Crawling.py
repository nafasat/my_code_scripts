#!/usr/bin/python3

import requests
import dns.resolver
import sys
import argparse

# create parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("domain", type=str,
                    help="display the details of a domain")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="details of header also")
parser.add_argument("-o", "--option",
                    help="pass [header] or [record] or [all]")
parser.add_argument("-p", "--protocol",
                    help="pass [https] or [http]")

args = parser.parse_args()


def check_records(dom, record):
    try:
        record_result = dns.resolver.resolve(dom, record)
        for data in record_result:
            print(dom, '\t', record, '\t', data)
    except Exception as e:
        print(dom, '\t', record, '\t', 'NoAnswer')


def domain_header(url):
    try:
        url_header = requests.get(url)
    except Exception as e:
        print("connection failure, Please check manual")
        sys.exit(1)
    print('ResponseCode\t: %-15s' % url_header.status_code)
    print('ResponseCode\t: %-15s' % url_header.status_code)
    for Keys in url_header.headers:
        print("%-15s: %-15s" % (Keys, url_header.headers[Keys]))


def check_domain_header(dom):
    if args.protocol == 'https':
        print("Output for Https Only")
        domain_header('https://' + dom)

    elif args.protocol == 'http':
        print("Output for Http Only")
        domain_header('http://' + dom)
    else:
        print("Output for Https Only")
        domain_header('https://' + dom)
        print("\nOutput for Http Only")
        domain_header('http://' + dom)


if args.option == 'header':
    check_domain_header(args.domain)

elif args.option == 'record':
    for i in ['A', 'CNAME', 'MX']:
        check_records(args.domain, i)

elif args.option == 'all':
    check_domain_header(args.domain)
    print("\t")
    for i in ['A', 'CNAME', 'MX']:
        check_records(args.domain, i)

else:
    print("Test fail")
