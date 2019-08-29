#!/usr/bin/env Python3

import sys

fname = open(sys.argv[1])

gene_list = []
#Weed out the unwanted things
for i, line in enumerate(fname):
    if line.startswith("#"):
        continue
    
    col = line.rstrip("\n").split()
    chrom = col[0]
    types = col[2]
    gene_start = int(col[3])
    gene_stop = int(col[4])
    gene_name = col[13]
    if chrom == "3R" and types == "gene":
        if 'gene_biotype "protein_coding"' in line:
            gene_list.append((gene_start, gene_stop, gene_name))
# gene location(start,stop), gene name

low = 0
high = len(gene_list) - 1
mid = 0
number_iterations = 0

#binary code
pos_search = 21378950

while (low <= high):
    mid = int((high+low)/2)
    number_iterations += 1
    if (pos_search < gene_list[mid][0]):
        gene_list = gene_list[low:mid+1]

    elif (pos_search > gene_list[mid][0]):
       low = gene_list[mid][0]
       gene_list = gene_list[mid:high+1]
    else:
        print(gene_list[mid])
        print(number_iterations)
        #print(gene_list(range([mid] - 20, [mid] + 20) + " " + number_iterations)