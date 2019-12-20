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

cfu=df["CFU"].values
poly=df["poly"].values
data2={'x' : cfu, 'y' : poly}
kmeans_df=pd.DataFrame(data2, columns=['x','y'])


kmeans=KMeans(n_clusters=5).fit(kmeans_df)
centroids= kmeans.cluster_centers_

fig, ax=plt.subplots()
plt.scatter(kmeans_df['x'], kmeans_df['y'], c= kmeans.labels_.astype(float), s=30, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=30)
ax.set_ylabel("CFU")
ax.set_xlabel("poly")
fig.tight_layout()
fig.savefig("kmeans.png")