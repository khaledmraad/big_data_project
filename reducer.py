#!/usr/bin/env python3
import sys
Total = 0
oldKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisNb = data_mapped
    if oldKey and oldKey != thisKey:
        print (oldKey, "\t", Total)
        oldKey = thisKey
        Total = 0
    oldKey = thisKey
    Total += int(thisNb)
if oldKey != None:
    print (oldKey,"\t", Total)