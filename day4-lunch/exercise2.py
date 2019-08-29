#!/usr/bin/env python3

"""
Usage: exercise2.py <ctab>
Plot FPKM
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep = "\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep = "\t", index_col="t_name")

fpkm1 = np.log2(ctab1.loc[:,"FPKM" ]+ 0.01)
fpkm2 = np.log2(ctab2.loc[:,"FPKM"] + 0.01)

m,b = np.polyfit(fpkm1,fpkm2,1)
x = np.linspace(fpkm1.min(), fpkm1.max(),2)

fig, ax = plt.subplots()
ax.scatter(y=fpkm1,x=fpkm2, s = 1, alpha=0.3)
ax.plot(x,[(m*x1) + b for x1 in x], color = "green", label = 'y = %sx + %s' % (str(m)[:5], str(b)[:5]))
ax.set_title("Frequency of FPKMs")
ax.set_xlabel("log[FPKM]")
ax.set_ylabel("Percent of Frequency")
ax.legend(loc = "upper left", fontsize = 8)
fig.savefig("exercise2.png")
plt.close(fig)
