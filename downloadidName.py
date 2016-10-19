# -*- coding: utf-8 -*- 
import sys
import os
import urllib2
import urllib
import time

aimurl = 'http://pinyin.sogou.com/dict/detail/index/'  
for index in xrange(70000,int(sys.argv[1])):
	for _ in range(5):
		try:
			f = urllib2.urlopen(aimurl+str(index), timeout=20) 
			data = f.read() 
			oldspot = data.find("dict_detail_title")
			while(data[oldspot]!='>'):
				oldspot = oldspot + 1
			oldspot += 1
			spot = oldspot
			while(data[spot]!='<'):
				spot = spot + 1
			file = open("word/idName.txt","a")
			if data[oldspot:spot] != '':
				file.write(str(index)+": "+data[oldspot:spot]+"\n")
			file.close()
			break
		except Exception,Argument:
			continue
print "end"