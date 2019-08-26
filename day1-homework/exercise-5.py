#!/usr/bin/env Python3

import sys


series = open(sys.argv[1])
#series = sys.stdin
count = 0
#total mapq
lines = 0
#number of lines
for alignment in series:
    fields = alignment.split("\t")
    number = fields[4]
    count += int(number)
    lines += 1

average = count / lines


print(average)
    