#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

intersect1 = open(sys.argv[1])
intersect2 = open(sys.argv[2])

promoter = 0
exon = 0
intron = 0
misc = 0

promoter2 = 0
exon2 = 0
intron2 = 0
misc2 = 0

for line in intersect1:
    rcol = line.rstrip("\n").split()
    if rcol[3] == "promoter":
        promoter += 1
    elif rcol[3] == "exon":
        exon += 1
    elif rcol[3] == "intron":
        intron += 1
    else:
        misc += 0

for line2 in intersect2:
    rcol2 = line2.rstrip("\n").split()
    if rcol2[3] == "promoter":
        promoter2 += 1
    elif rcol2[3] == "exon":
        exon2 += 1
    elif rcol2[3] == "intron":
        intron2 += 1
    else:
        misc2 += 0
# print("promoter: " + str(promoter2))
# print("exon: " + str(exon2))
# print("intron: " + str(intron2))
# print("non-matching: " + str(misc2))

names = ["promoter", "intron", "exon"]
values1 = []
values2 = []
values1.append(promoter)
values1.append(intron)
values1.append(exon)
values2.append(promoter2)
values2.append(intron2)
values2.append(exon2)
# print(values1)
print(promoter, intron, exon)

file1 = open(sys.argv[3])
file2 = open(sys.argv[4]) 

gained = 0 
lost = 0 
print(values2)
for line in file1:
    gained += 1

for line in file2:
    lost += 1

x_value = np.arange(len(names))
width = 0.3

fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20, 10))
axes = axes.flatten()
axes[0].bar(x=["Lost", "Gained"], height = [lost, gained])
axes[0].set_xlabel(" CTCF Binding Sites")
axes[0].set_ylabel("Number of Sites")
axes[1].bar(x= x_value + width/2, height = list(values1), width = width, color = "red", label = "G1E")
axes[1].bar(x= x_value - width/2, height = list(values2), width = width, color = "blue", label = "ER4")
axes[1].set_xticks(x_value)
axes[1].set_xticklabels(names)
axes[1].legend()
axes[1].set_xlabel("Features")
axes[1].set_ylabel("Number of Sites")
fig.suptitle("CTCF ChIP-Seq in Mice")
fig.savefig("week6_plot.png")
plt.close(fig)

