#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

f = open(sys.argv[1])

loc = []

for line in f:
    if line.startswith("motif_id"):
        continue
    col = line.rstrip("\n").split()
    if col != []:
        loc.append(int(col[3]))

fig, ax = plt.subplots()
sns.distplot(loc, hist= True, rug = True, kde = True)
x_string_labels = ['0','10000000','20000000','30000000','40000000','500000000','60000000']
ax.set_xlim(0,62000000)
ax.set_xticklabels(x_string_labels)
ax.set_title("Top 100 ER4 Matched Motifs")
ax.set_ylabel("Frequency")
ax.set_xlabel("Position")
fig.tight_layout()
plt.show()
fig.savefig("matchmotifgraph.png")
plt.close(fig)