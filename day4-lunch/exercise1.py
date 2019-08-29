#!/usr/bin/env python3

"""
Usage: ./01-hist.py <ctab>
Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd

fpkms = []

ctab = pd.read_csv(sys.argv[1], sep = "\t")
goi = ctab.loc[:,"FPKM"] > 0
my_data = np.log2(ctab.loc[goi,"FPKM"])

a = float(sys.argv[2])
center = float(sys.argv[3])
scale = float(sys.argv[4])

x = np.linspace(my_data.min(), my_data.max(), 100)
y = stats.skewnorm.pdf(x,a,center,scale)

 
fig, ax = plt.subplots()

ax.hist(my_data,bins = 100,density = True)
ax.plot(x,y)
ax.set_title("Frequency of FPKMs")
ax.set_xlabel("log[FPKM]")
ax.set_ylabel("Percent of Frequency")
fig.savefig("fpkms.png")
plt.close(fig)