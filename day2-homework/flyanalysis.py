#!/usr/bin/env Python3

import sys

for line in (sys.stdin):
    if "DROME" not in line: 
        continue
    if "FBgn" not in line:
        continue
    col = line.rstrip("\n").split()
    acn = col[-2]
    fbg = col[-1]

    print(fbg,"\t",acn)