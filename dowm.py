#!/usr/bin/env python
#python

import os
import urllib2

url='http://dumps.wikimedia.org/other/pagecounts-raw/2014/2014-02/'
if os.path.isfile("url.txt"):
	url_list=open('url.txt')
	for line in url_list:
		name=line.split()[0].rstrip(',')
		per_url=url+name#every url
        	file_name=name.rstrip(name.split('-')[2])+name.split('-')[2][:2]
        	#cnt+=1
        	#print per_url,file_name
		f=urllib2.urlopen(per_url)
		with open('2014-02/'+file_name, "wb") as down:
			down.write(f.read())

