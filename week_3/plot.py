#!/usr/bin/env python3

import sys 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

snp = open(sys.argv[1])

read_depth = []
quality = []
frequency = []
ai = {}

for line in snp:
    if line.startswith("#"):
        continue
    col = line.rstrip("\n").split("\t")
    fields = col[7].rstrip("\n").split(";")
    dp = fields[7].rstrip("\n").split("=")
    read_depth.append(dp[1])
    
    qual = int(float(col[5]))
    quality.append(qual)
    
    af = fields[3].rstrip("\n").split("=")
    frequency.append(af[1])
    
    cola = fields[41].rstrip("\n").split("|")
    a = cola[1]
    if a in ai:
        ai[a] += 1
    else:
        ai[a] = 1
    
    
    
fig,((ax1, ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2)

ax1.hist(read_depth,bins = 100,density = True)
ax1.set_title("Read Depth of SNPs",size=15)
ax1.set_xlabel("Read Depth")
for tick in ax1.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(5)
ax1.set_ylabel("Postion of SNP")

ax2.hist(quality, bins = 50,density = True, range= (0,2500))
ax2.set_title("Read Quality of SNPs",size=15)
ax2.set_xlabel("Read Quality",size=10)
ax2.set_ylabel("Postion of SNP",size=10)

ax3.hist(frequency, bins = 50,density = True)
ax3.set_title("Allele Frequency of SNPs", size =15)
ax3.set_xlabel("Allele Frequency",size=10)
for tick in ax3.get_xticklabels():
    tick.set_rotation(90)
    tick.set_size(8)
ax3.set_ylabel("Postion of SNP",size=10)

plt.bar(range(len(ai)),list(ai.values()), align = 'center')
plt.xticks(range(len(ai)),list(ai.keys()), rotation= "vertical", size=8)
ax4.set_title("SNP Annotation Impact", size=15)
ax4.set_xlabel("Annotation impact",size=10)
ax4.set_ylabel("Frequency",size=10)

fig.set_size_inches(40, 14)
plt.tight_layout()
fig.savefig("aplot.png",dpi=200)
plt.close(fig)
