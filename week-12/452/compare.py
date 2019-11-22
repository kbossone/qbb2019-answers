#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

n452 = open(sys.argv[1])
n454 = open(sys.argv[2])

methylation452 = {}
methylation454 = {}

upmeth452 = []
upmeth454 = []

for line in n452:
   col = line.rstrip("\n").split()
   methylation452[col[3]] = col[4]
   
for line in n454:
   col = line.rstrip("\n").split()
   methylation454[col[3]] = col[4]

for start in methylation452:
    if start in methylation454:
        if methylation452[start] == 'Z' and methylation454[start] == 'z':
            upmeth452.append(start)
        elif methylation452[start] == 'z' and methylation454[start] == 'Z':
            upmeth454.append(start)

print(upmeth454)