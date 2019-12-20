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

diff_exp_high = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2)) >=2
diff_exp_low = (((df['CFU']+df['unk'])/2)/((df['poly']+df['int'])/2)) <= 0.5

diff_exp_genes = df[diff_exp_high | diff_exp_low]

for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    if sp.ttest_rel(sample1, sample2).pvalue <= 0.05:
            print(gene_name,sp.ttest_rel(sample1, sample2).pvalue)