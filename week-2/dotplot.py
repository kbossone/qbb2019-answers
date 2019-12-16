#!/usr/bin/env python3

import sys 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

lastz = open(sys.argv[1])

tstart = []
cstart = []
tend = []
cend = []
lists = []
rstarts = []
rends = []
dicto = {}
clength = []

for line in lastz:
    if "#" in line:
        continue
    col = line.rstrip("/n").split()
    if col[7] != "-":
        rstart= int(col[4])
        rend = int(col[5])
        costart = int(col[9])
        coend = int(col[10])
        length = abs(coend - costart)
        dicto[int(rstart)] = [rstart, rend, length]
        
for key in sorted(dicto):
    rstarts.append(dicto[key][0])
    rends.append(dicto[key][1])
    clength.append(dicto[key][2])
    
fig, ax = plt.subplots()
ax.plot()
fig.suptitle("Spades K21 Contigs Dotplot")
count = 0
for i in range(len(rstarts)):
    ax.scatter(x=[count, count+clength[i]], y=[rstarts[i], rends[i]], alpha=0.4)
    count += int(clength[i])
ax.set_xlabel("K21 Contigs length (bp)")
ax.set_ylabel("Reference Length (bp)")
plt.ylim((0,120000))

fig.savefig("Spades_Part_3_dotplot.png")
plt.close(fig)
        
    