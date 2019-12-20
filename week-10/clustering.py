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

link = linkage(df, method='single', metric = 'euclidean')
leaf = leaves_list(link)

df2= df.transpose()
link2 = linkage(df2, method='single', metric = 'euclidean')
leaf2 = leaves_list(link2)

df3 = df.iloc[leaf,:]
df4 = df3.iloc[:, leaf2]

fig, ax = plt.subplots()
plt.pcolor(df4)
plt.yticks(np.arange(0.5, len(df4.index), 1), df4.index)
plt.xticks(np.arange(0.5, len(df4.columns), 1), df4.columns)
for tick in ax.get_yticklabels():
   tick.set_size(2)
fig.savefig("Heat-map.png")
plt.close(fig)