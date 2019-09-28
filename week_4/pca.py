#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

eigen = open(sys.argv[1])

third = []
fourth = []

for line in eigen:
    col = line.split(" ")
    three = float(col[2])
    four = float(col[3])
    third.append(three)
    fourth.append(four)

fig, ax = plt.subplots()
ax.scatter(third, fourth)
fig.suptitle("PCA")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")

fig.savefig("pca.png")
plt.close() 


