#!/usr/bin/env python3
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

metadata = sys.argv[1]
ctab_dir = sys.argv[2]
fpkms = {}
for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    fields = line.strip().split(",")
    srr_id = fields[0]
    info = '_'.join(fields[1:])
    ctab_path = os.path.join(ctab_dir, srr_id,"t_data.ctab")
    print(ctab_path)
    
    df = pd.read_csv(ctab_path, sep="\t",
                    index_col="t_name")
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[info] = df.loc[:,"FPKM"]

df_fpkms = pd.DataFrame(fpkms)
print(df_fpkms.describe())
pd.DataFrame.to_csv(df_fpkms,"all.csv")