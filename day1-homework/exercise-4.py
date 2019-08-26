#!/usr/bin/env Python3

import sys


series = open(sys.argv[1])
#series = sys.stdin

wild_count = 0
for alignment in series:
    while wild_count < 11:
        column = alignment.split("\t")
        chromosome = column[2]
        wild_count += 1
        print(chromosome)