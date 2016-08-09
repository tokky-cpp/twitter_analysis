#encode:utf-8
import datetime
import sys
count = {}

t = datetime.datetime.today()
if sys.argv[1]!=None:
    back = int(sys.argv[1])
    t -= datetime.timedelta(days=back)

stop_words = []
for s in open("stop_words.txt","r"):
    stop_words.append(s.rstrip())

today = "%04d%02d%02d"%(t.year,t.month,t.day)
for line in open("%s.wc"%today,"r"):
    words = line.split(' ')
    for w in words:
        if w in stop_words: continue
        count.setdefault(w,0)
        count[w] += 1
for k,v in sorted(count.items(), key=lambda x:x[1]):
    print k,v


print sum(count.values()),"words"
print len(count),"kinds"

#for s in stop_words:
#    print s
#print count
#for c in count:
#    print c,count[c]
