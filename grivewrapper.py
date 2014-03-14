#!/usr/bin/env python
###############################################################################
# Author: Ben Lutgens
# Purpose: Periodically check to see if internet connection is
# available and if so, run grive to sync google drive to local ~/Grive dir
# Date: 14/Mar/2014
#
###############################################################################


import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://google.com',timeout=2)
        print "It works!"
        return True
    except urillib2.URLError as err: pass
    print "It didn't work!"
    return False

if __name__ == "__main__":
    internet_on()
