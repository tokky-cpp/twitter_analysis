#encode:utf-8
#sample command 'python clean.py TL.txt TL_clear.txt'
import re
import sys


w = open(sys.argv[2],"w")
for line in open(sys.argv[1],"r"):
    ret = re.sub(r'http[s]?[\S]*','',line)
    ret = re.sub(r'@[\S]*',' ',ret)
    w.write(ret)

w.close()



