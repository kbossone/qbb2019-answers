#!/usr/bin/env python3

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


gene_name = sys.argv[1]
fpkm_file = sys.argv[2]
df = pd.read_csv(fpkm_file, index_col="t_name")

goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop(columns="gene_name")
#goi is boolean and is choosing for what is true. filtered genes of interist
filtered_fpkms = fpkms.loc[goi,:]
#list comp in order to make list out of a different list
male_ids = [y for y in list(filtered_fpkms) if y.startswith('male')]
male_transcripts = np.log2(filtered_fpkms[male_ids] + 0.001)
female_ids = [x for x in list(filtered_fpkms) if x.startswith('female')]
female_transcripts = np.log2(filtered_fpkms[female_ids] +0.001)

male_x_axes = [y[5:] for y in male_ids]
female_x_axes = [x[7:] for x in female_ids]
# print(fpkms.loc[goi,:)

fig, (ax1, ax2) =plt.subplots(nrows=2)
ax1.boxplot(male_transcripts.T)
ax1.set_title("Male Embryo FPKMs")
ax1.set_xticklabels(male_x_axes, fontsize=7)
ax1.set_ylabel("Transcript count of Sxl")
ax2.boxplot(female_transcripts.T)
ax2.set_title("Female Embryo FPKMs")
ax2.set_xticklabels(female_x_axes, fontsize=7)
ax2.set_ylabel("Transcript count of Sxl")
plt.tight_layout()
fig.savefig("boxplot.png")
plt.close(fig)