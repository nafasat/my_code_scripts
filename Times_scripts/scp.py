#!/usr/bin/env python3

import os


class Base:

    def remote_copy(self, remote_ip, username, src_path, dest_path):
        self.remote_ip = remote_ip
        self.username = username
        self.src_path = src_path
        self.dest_path = dest_path
        command = 'scp -r ' + self.username + '@' + self.remote_ip + ':' + self.src_path + ' ' + self.dest_path
        print(command)
        os.popen(command)
        #if os.popen(command) == 0:
         #   return True
        #else:
        #    return False


a = Base()
a.remote_copy('172.29.145.252', 'UserName', '/var/lib/nginx/state/backend*VIP.conf', '/tmp/1234')
