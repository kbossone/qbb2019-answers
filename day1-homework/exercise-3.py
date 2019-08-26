#!/usr/bin/env Python3

import sys


series = open(sys.argv[1])
#series = sys.stdin
count = 0
for alignment in series:
    fields = alignment.split("\t")
    if fields[2] == "*":
        continue
    else:
        count += 1

print(count)
    
series.seek(0)
hit_count = 0
for alignments in series:
    fields = alignments.split("\t")
    status = fields[11:]
    for column in status:
        if "NH:i:1" in column:
            hit_count += 1
        
print(hit_count)