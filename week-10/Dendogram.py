#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import scipy.stats as sp

data = open(sys.argv[1])

df = pd.read_csv(data, sep = "\t", index_col = 0)
df2=df.transpose()

link = linkage(df2, method='average', metric = 'euclidean')
leaf = leaves_list(link)

fig, ax = plt.subplots()
ax = dendrogram(link, truncate_mode = 'lastp', labels = df2.index, leaf_rotation = 90)
plt.tight_layout()
fig.savefig("Dendrogram.png")
plt.close(fig)