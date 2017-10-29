#!/usr/bin/env python

import os

def get_whois(url):
    command = 'whois'+str(url)
    process = os.popen(command)
    req = str(process.read())
    return req

#print 'Details: ',get_whois('google.com')
