#!/usr/bin/env Python3

import sys


series = open(sys.argv[1])
#series = sys.stdin
pos_range = list(range(10000,20001))
counts = 0
for line in series:
    fields = line.split("\t")
    if fields[2] == "2L":
        if int(fields[3]) in pos_range:
            counts += 1

print(counts)