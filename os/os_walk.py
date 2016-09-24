#!/usr/bin/python
#Function: illustrate the usage of os.walk
import os
for directory,dirnames,filenames in os.walk(".",topdown=False):
	print 'directory:%s' % directory
	print 'dirnames:%s' % dirnames
	print 'filenames:%s' % filenames
