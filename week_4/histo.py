#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

freq = open(sys.argv[1])

frequ = []

for line in freq:
    if "CHR" in line:
        continue
    col = line.split()
    values = float(col[4])
    frequ.append(values)

fig, ax = plt.subplots()
ax.hist(frequ, bins = 100, density = True)
ax.set_title("Histogram",size=15)
ax.set_xlabel("Position",size=10)
ax.set_ylabel("Frequency",size=10)

fig.savefig("histo.png")
plt.close() 


