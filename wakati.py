#!/usr/bin/env python                                                         
# -*- coding:utf-8 -*-
import MeCab
import sys
import datetime
### Constants
#MECAB_MODE = 'mecabrc'
#PARSE_TEXT_ENCODING = 'utf-8'

t = datetime.datetime.today()
if sys.argv[1]!=None:
    back = int(sys.argv[1])
    t -= datetime.timedelta(days=back)

day = "%04d%02d%02d"%(t.year,t.month,t.day)
w = open("%s.wc"%day,"w")
nouns = []
tagger = MeCab.Tagger()
for line in open("%s.clear"%day,"r"):
    #res = tagger.parseToNode(line)
    result = tagger.parse(line)

    for r in result.split('\n'): 
        arr = r.split(",")
    
        word = arr[0].split("\t")
        if(len(word)>=2): print word[0],word[1]
        if len(word)>=2 and word[1]=="名詞":
            nouns.append(word[0])
            w.write(word[0]+' ')
#            print word[0],word[1]

#for n in nouns:
#    print n

#print nouns
w.close()
