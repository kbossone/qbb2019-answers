#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep = "\t", index_col = "t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep = "\t", index_col = "t_name")

fpkm = {name1: ctab1.loc[:, "FPKM"],
      name2: ctab2.loc[:, "FPKM"] }

df = pd.DataFrame(fpkm)
df += 1

r=df.loc[:,name1]
g=df.loc[:,name2]

m= np.log2(r/g)
a= .5*np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter( x=a, y=m, s = 3, alpha = .3)
ax.set_title("SRR072916 and SRR072915")
ax.set_xlabel("m")
ax.set_ylabel("a")
fig.savefig("ma_plot.png")
plt.close(fig)