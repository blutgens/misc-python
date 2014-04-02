#!/usr/bin/env python
###############################################################################
# Author: Ben Lutgens
# Purpose: 
# Date:
#
###############################################################################

#for a in [1, 2]:
#    for b in ['a', 'b']:
#        print a, b

#import os
#if os.path.isdir("/tmp"):
#    print "/tmp is a directory"
#else:
#    print "/tmp is NOT a directory"

class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def set_ip(self, ip):
        self.ip = ip
    def set_hostname(self, hostname):
        self.hostname = hostname
    def ping(self, ip_addr):
        print "Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname)

if __name__ == '__main__':
    server = Server('10.10.30.133', 'derpy')
    server.ping('10.10.30.1')

