#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#~/qbb2019-answers/results/stringtie/SRR072893/t_data.ctab
# need chromosome[1] start[3] end[4] name[5]
# start end + 500


df = pd.read_csv(open(sys.argv[1]), sep="\t")

genes=df.loc[:,(("t_name", "start","end","chr","strand"))]

for i,t in genes.iterrows():
    if t.loc["strand"] == "+":
        prom1 = int(t.loc["start"]) + 500
        prom2 = int(t.loc["start"]) - 500
        a = t.loc["chr"]
        t_name = t.loc["t_name"]
        if prom2 > 0: 
            print(a,prom2,prom1,t_name,sep="\t")
        else:
            print(a,t.loc["start"],prom1,t_name,sep="\t")

    elif t.loc["strand"] == "-":
        prom3 = int(t.loc["end"]) + 500
        prom4 = int(t.loc["end"]) - 500
        a = t.loc["chr"]
        t_name = t.loc["t_name"]
        if prom4 > 0:
            print(a,prom4,prom3,t_name,sep="\t")
        else:
            print(a,t.loc["start"],prom3,t_name,sep="\t")