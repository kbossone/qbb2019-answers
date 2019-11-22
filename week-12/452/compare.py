#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

n452 = open(sys.argv[1])
n454 = open(sys.argv[2])

list452 = []
list454 = []
uniq452 = []
uniq454 = []

for line in n452:
   col = line.rstrip("\n").split()
   if col[4] == "Z":
       list452.append(col[3])
   
for line1 in n454:
   col1 = line1.rstrip("\n").split()
   if col1[4] == "Z":
       list454.append(col1[3])
   
# for item in list452:
#     if item not in list454:
#         uniq452.append(item)

for item in list454:
    if item not in list452:
        uniq454.append(item)

print(uniq454)