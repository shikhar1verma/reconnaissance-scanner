#!/usr/bin/env python
'''
this will provide the website's top level
domain name.
'''
from tld import get_tld             #tld help us to get the top level domain name

def get_domain_name(url):               #this function give us the top level domain name

	domain_name = get_tld(url)
	return domain_name

#print get_domain_name('https://www.facebook.com')
