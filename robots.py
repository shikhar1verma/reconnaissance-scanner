#!/usr/bin/env python
'''
this script will tell ua about the
robots.txt file of website.
robots.txt is the file which webcrawlers
dont crawl.
'''
from urllib import urlopen

def robots_txt(url):                                            #this will open the robots.txt
    if url.endswith('/'):
        path = url
    else:
        path = url+'/'
    try:
        if 'https' in path:                                     #first it will check for https
            req = urlopen(path+'robots.txt',data = None)
            return req.read()
        return (urlopen(path+'robots.txt',data = None)).read()  #if user input is http then directly try to open
    except Exception as e:                                      #if https give some error it will try to open with http
        index = path.find('://')
        path = path[:index-1] + path[index:]
        req = urlopen(path+'robots.txt',data = None)
        return req.read()
        print 'Error is: ',str(e)

#print 'file is: '+str(robots_txt('https://www.sus.edu.in/'))
