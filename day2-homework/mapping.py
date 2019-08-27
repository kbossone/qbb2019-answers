#!/usr/bin/env Python3

import sys

# ../results/stringtie/SRR072915/t_data.ctab
genes_of_interest = {}

for line in open(sys.argv[1]):
    col = line.rstrip("\n").split("\t")
    genes_of_interest[col[0]] = col[1]

for line in open(sys.argv[2]):
    col = line.rstrip("\n").split("\t")
    gene_name = col[8]
    if gene_name in genes_of_interest:
        result = genes_of_interest[gene_name]
        print(result, "\t", line)
    elif sys.argv[3] == "bad":
        print("Bad input", "\t", line)
    else:
        continue
