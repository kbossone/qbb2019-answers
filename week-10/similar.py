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
data2 = df[['CFU','poly']]

kmeans = KMeans(n_clusters=5).fit(data2)
centroids = kmeans.cluster_centers_

labels = list(kmeans.labels_)
gene = list(data2.index.values)

goi_index = gene.index(sys.argv[2])
goi_cluster = labels[goi_index]

relgenes=[]

for i, gene in enumerate(gene):
    if labels[i] == goi_cluster:
        print(gene)