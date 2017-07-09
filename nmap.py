#!/usr/bin/env python
'''
this script check for the open ports
and service which are running on that
port.we are doing port scanning with this
'''
import os
import pdb

def get_nmap(options,url):                  #this function will scan the ports of the website
	command= 'nmap '+options+' '+url
	process = os.popen(command)
	results = str(process.read())
	return results

#print 'the IP of google is: '+str(get_nmap('-F','www.google.com'))

