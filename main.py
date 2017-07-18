#!/usr/bin/env python
'''
this script will access all the function
of reconnaissance scanner.And give the url
and the website name to the script and it
will scan the required fields of websites
and store it in a .txt file in a folder.
'''
from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots import *
from whois import *


root_dir = 'websites'           #creating directory websites
create_dir(root_dir)

def gather_info(name,url):                      #gathering the information through other scripts
    robotsTXT = robots_txt(url)
    domain_name = get_domain_name(url)
    whois = get_whois(domain_name)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F',ip_address)

    create_report(name,url,domain_name,nmap,robotsTXT,whois,ip_address)

def create_report(name,url,domain_name,nmap,robotsTXT,whois,ip_address):   #put the gathered information in required files
    project_dir = root_dir + '/' + name
    create_dir(project_dir)

    write_file(project_dir + '/full_url.txt',url )
    write_file(project_dir + '/domain_name.txt',domain_name )
    write_file(project_dir + '/nmap.txt',nmap )
    write_file(project_dir + '/robots.txt',robotsTXT )
    write_file(project_dir + '/whois.txt',whois )
    write_file(project_dir + '/ip_address.txt',ip_address )

gather_info('google','https://www.google.com')                  #giving the input of website name and url
