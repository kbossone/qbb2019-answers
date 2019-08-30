#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

t_name = sys.argv[1]
samples = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[5]
def sex_sorter(sex):
   soi = samples.loc[:,"sex"] == sex
   stages = samples.loc[soi, "stage"]

   fpkms = pd.read_csv(sys.argv[3], index_col="t_name")

   my_data = []
   for stage in stages:
       my_data.append(fpkms.loc[t_name,sex+ '_' +stage])
   return my_data

def rep_sex_sorter(sex):
    samples = pd.read_csv(sys.argv[4])
    soi = samples.loc[:,"sex"] == sex
    srr_ids = samples.loc[soi,"sample"]
    my_data = []
    for srr_id in srr_ids:
       # my_data_replicates(replicates.loc[t_name, sex+ '_' +stage])
       #my_data.append(fpkms.loc[t_name,srr_id])

       ctab_path = os.path.join(ctab_dir, srr_id,
                               "t_data.ctab")
       #print(ctab_path)
       df = pd.read_csv(ctab_path, sep="\t",
                       index_col="t_name")
       my_data.append(df.loc[t_name, "FPKM"])
    return my_data

male_data = sex_sorter("male")
rep_male = rep_sex_sorter("male")
female_data = sex_sorter("female")
rep_female = rep_sex_sorter("female")
# print(my_data)

#This down is making the graph
labels = ["Male","Female"]
labels2 = ["10","11","12","13","14A","14B","14C","14D"]

fig,ax = plt.subplots()
ax.plot(male_data, color = "blue")
ax.plot(female_data, color = "red")
ax.plot(range(4,8), rep_male, 'o', color="blue")
ax.plot(range(4,8), rep_female, 'o', color="red")
ax.set_title("Male and Female mRNA abundance for Sxl Transcripts")

ax.set_xlabel("Embryonic Stage")
ax.set_xticklabels(labels2, rotation='vertical')
ax.set_xticks(np.arange(len(labels2)))

ax.set_ylabel("mRNA abundance")
plt.legend(labels=labels, loc="center left", bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
fig.savefig("timecourse.png")
plt.close(fig)