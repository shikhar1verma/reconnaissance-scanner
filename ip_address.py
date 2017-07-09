#!/usr/bin/env python
'''
This script uses the host command
to get the ip address.host is a
simple utility for performing DNS
lookups. It is normally
used to convert names to IP
addresses and vice versa.
'''

import os
import pdb

def get_ip_address(url):                        #this will give us the IP address
	command= 'host ' + url
	process = os.popen(command)
	results = str(process.read())
	marker = results.find('has address')+12
	return results[marker:].splitlines()[0]

#print 'the IP of google is: '+str(get_ip_address('google.com'))

