#!/usr/bin/env python3
"""USAGE: ./ """
import sys
import matplotlib.pyplot as plt
import numpy as np

blastn=open(sys.argv[1])

for line in blastn:
    col=line.rstrip("\n").split("\t")
    print (">" + col[0])
    print (col[1])