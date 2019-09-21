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

    
    
    
fig, ax = plt.subplots(4)

ax[0].hist(read_depth,bins = 100,density = True)
ax[0].set_title("Read Depth of SNPs")
ax[0].set_xlabel("Read Depth")
ax[0].set_ylabel("Postion of SNP")

ax[1].hist(quality, bins = 50,density = True, range= (0,2500))
ax[1].set_title("Read Quality of SNPs")
ax[1].set_xlabel("Read Quality")
ax[1].set_ylabel("Postion of SNP")

ax[2].hist(frequency, bins = 50,density = True)
ax[2].set_title("Allele Frequency of SNPs")
ax[2].set_xlabel("Allele Frequency")
ax[2].set_ylabel("Postion of SNP")

plt.bar(range(len(ai)),list(ai.values()), align = 'center')
plt.xticks(range(len(ai)),list(ai.keys()), rotation= 'vertical', size=6)
ax[3].set_title("Allele Frequency of SNPs")
ax[3].set_xlabel("Allele Frequency")
ax[3].set_ylabel("Postion of SNP")


# plt.tight_layout()
fig.savefig("plot1.png")
plt.close(fig)
