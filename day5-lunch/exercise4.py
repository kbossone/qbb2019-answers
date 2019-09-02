#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy
#./exercise4.py ~/qbb2019-answers/results/stringtie/SRR072893/t_data.ctab H3K4me1.tab H3K4me3.tab H3K9me3.tab 
#FBtr0302347

his_dic = {}

fpkms = sys.argv[1]
h1 = sys.argv[2]
h2 = sys.argv[3]
h3 = sys.argv[4]

df = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t",index_col=0,header=None)
df3 = pd.read_csv(sys.argv[3], sep="\t",index_col=0,header=None)
df4 = pd.read_csv(sys.argv[4], sep="\t",index_col=0,header=None)

histones = {"FPKM": df.loc[:,"FPKM"],
                "H3K4me1": df2.iloc[:,-1],
                "H3K4me3": df3.iloc[:,-1],
                "H3K9me3": df4.iloc[:,-1]}
                
histone_df = pd.DataFrame(histones)
#print(histone_df)
model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data = histone_df)
ols_result = model.fit()
print(ols_result.summary())
