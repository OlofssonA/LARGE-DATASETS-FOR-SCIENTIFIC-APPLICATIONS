#!/usr/bin/env python
import sys
import pysam


try:
    samfile = pysam.AlignmentFile("-", "rb")
    for read in samfile.fetch():
        if abs(int(read.reference_length or 0))>1000:
        print "%s\t 1" % read.reference_length
    samfile.close()
except ValueError:
    pass
    
    
    
import pysam
import time
start_time = time.time()
big=0
count=0
count_long=0
for i in range(0,10):
    samfile = pysam.AlignmentFile("/home/ubuntu/GenomeData/"+ListanSorted[i], "rb")
    f = open('/home/ubuntu/GenomeData/testout.txt', 'wb')
    for read in samfile.fetch():
        count+=1
        if int(read.reference_length or 0)>big:
            big=int(read.reference_length)
        if abs(int(read.reference_length or 0))>1000:
            print read.reference_length
            print read
            print >>f, read.reference_length
            count_long+=1
samfile.close()
f.close()
print("Klar, Tid: %s seconds " % (time.time() - start_time))
print "Största readen: " + str(big)
print "Antalet Reads: " + str(count)
print "Antalet long Reads: " + str(count_long)
