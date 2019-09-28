#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


family = []
sample = []
pheno = {}
for i, line in enumerate(open(sys.argv[1])):
   if i == 0:
       continue
   fields = line.split("\t")
   id = str(fields[0]).split("_")
   family.append(id[0])
   sample.append(id[1])

df = pd.read_csv(sys.argv[1],sep = "\t")
df["FID"] = family
df["IID"] = sample
newdf = df.loc[:,["fid","iid"]]
pheno = df.iloc[:,1:47]
newdf1 = pd.concat((newdf,pheno), axis = 1)
pd.DataFrame.to_csv(newdf1, "phenotype.txt", sep="\t", index=False, na_rep= "NA")
