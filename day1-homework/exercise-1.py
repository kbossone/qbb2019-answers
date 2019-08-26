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