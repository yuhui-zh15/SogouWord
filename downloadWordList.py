# -*- coding: utf-8 -*- 
import sys
import os
import urllib2
import urllib
import time



url="http://pinyin.sogou.com/dict/download_txt.php?id="
beginTime = time.time()
if len(sys.argv) < 2:
	print "Too few arguments"
	print len(sys.argv)
	exit()
begin = 1 
end = 1
if int(sys.argv[1]) < 1:
	print "please enter a number over 1"

if(len(sys.argv) == 2):
	index = sys.argv[1]
	urllib.urlretrieve(url+str(index),"word/"+str(index)+".txt")
	print "downloading: "+str(index)+".txt"
	file = open("word/"+str(index)+".txt")
	firstLine = file.readline()
	if "<script>" in firstLine:
		file = open("word/"+str(index)+".txt","rb")
		file.close()
		os.remove("word/"+str(index)+".txt")
		print "removing: "+str(index)+".txt"
		exit()
	else:
		print index
		exit()
if(len(sys.argv) == 3):
	begin = int(sys.argv[1])
	end = int(sys.argv[2])
	print len(sys.argv)
	for index in xrange(begin,end):
		urllib.urlretrieve(url+str(index),"word/"+str(index)+".txt")
		print "downloading: "+str(index)+".txt"
		file = open("word/"+str(index)+".txt")
		firstLine = file.readline()
		if "<script>" in firstLine:
			file = open("word/"+str(index)+".txt","rb")
			file.close()
			os.remove("word/"+str(index)+".txt")
			print "removing: "+str(index)+".txt"
		else:
			print index

exitTime = time.time()
print "Spent "+str(exitTime-beginTime)+"s"