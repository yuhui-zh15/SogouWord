# -*- coding: utf-8 -*- 
import sys
import os
import time

beginTime = time.time()
s = set()

if(len(sys.argv) == 3):
    begin = int(sys.argv[1])
    end = int(sys.argv[2])
    for index in xrange(begin, end):
        namefile = open(str(index) + ".txt", "r")
        while True:
            line = namefile.readline()
            if (len(line) == 0): break
            fileid = line.split('\t')[0]
            print(fileid)
            try:
                wordfile = open("word/" + fileid + ".txt")
                while True:
                    word = wordfile.readline().decode('gbk')
                    if (len(word) == 0): break
                    s.add(word)
            except Exception:
                pass
        outfile = open("result/" + str(index) + ".txt", "w")
        for item in s:
            outfile.write(item.encode('utf-8'))
        outfile.write('\n')
        outfile.write('共' + str(len(s)) + '词')

exitTime = time.time()
print "Spent "+str(exitTime-beginTime)+"s"
