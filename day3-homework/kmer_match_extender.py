#!/usr/bin/env python3
from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)
k = int(sys.argv[1])
query = "../day3-homework/subset.fa"
f = open(query, 'r')
target = "../day3-homework/droYak2_seq.fa"
t = open(target, 'r')

freader = FASTAReader(f)
treader = FASTAReader(t)

kmers = {}
tseq = {}
last = {}

for ident, sequence in treader:
    sequence = sequence.upper()
    tseq[ident] = sequence
    for i in range(0,len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            kmers[kmer].append((i,ident))
        else:
            kmers[kmer] = [(i,ident)]

for ident, sequence in freader:
    sequence = sequence.upper()
    for j in range(0,len(sequence) - k + 1):
        kmer = sequence[j:j+k]
        if kmer in kmers:
            for ident, i in kmers[kmer]:
                taseq = tseq[ident]
                tlength = len(taseq)
                qseq = len(sequence)
                extended_kmer = kmer
                while True:
                    if extend_right:
                        if sequence[i + k + 1] == taseq[j + k + 1]:
                            j += 1
                            i += 1
                            extended_kmer += sequence[i + k + 1]
                        else:
                            extend_right = False
                    else:
                        #This is where I would add my extension to dictionary
                        break
                    if qseq == (i + k) or tlength == (j + k):
                        extend_right = False
                        
                        