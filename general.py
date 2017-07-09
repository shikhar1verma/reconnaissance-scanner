#!/usr/bin/env python
'''
this will simly used to make directory
and to write to a required file
'''

import os

def create_dir(drct):                       #this will create directory
	if not os.path.exists(drct):
		os.makedirs(drct)

def write_file(destination,data):           #this will write to a given file destination
		fil = open(destination,'w')
		fil.write(data)
		fil.close()
