#!/usr/bin/env python3
import sys
#--- get all lines from stdin ---
for line in sys.stdin:
#--- remove leading and trailing whitespace---
    line = line.strip()
    if len(line)==0:
    # Something has gone wrong. Skip this line.
        continue
    #--- split the line into words ---
    words = line.split()
    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        print(word,"\t",1)