#!/usr/bin/env python3

from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException

import sys
import re

def SSH_Command(Input_IP):
    import paramiko
    hostname = '172.29.145.252'
    port = 22
    username = 'nafasat.ahmed'
    password = 'king@321'
    command = "if [ -f /var/lib/nginx/state/backend"+Input_IP+".conf ]; then cat /var/lib/nginx/state/backend"+Input_IP+".conf; fi"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password, timeout=60)

    transport = ssh.get_transport()
    session = transport.open_session()
    session.set_combine_stderr(True)
    session.get_pty()
    try:
        session.exec_command(command)
    except Exception as e:
        print("Error")

    stdout = session.makefile('rb', -1)

    for i in stdout.readlines():
        print(i.strip().decode("utf-8"))

    session.recv_exit_status()
    ssh.close()


def check(input_ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    if re.search(regex, input_ip):
        SSH_Command(input_ip)
    else:
        print(stylize("%-10s\t[Invalid_VIP]" % input_ip, angry))


if __name__ == '__main__':
    print(sys.argv[1])
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
