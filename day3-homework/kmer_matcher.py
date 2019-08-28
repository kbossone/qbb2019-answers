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
kmer_l = []

for ident, sequence in freader:
    sequence = sequence.upper()
    for i in range(0,len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        
        if kmer in kmers:
            kmers[kmer].append((i,ident))
        else:
            kmers[kmer] = [(i,ident)]

for ident, sequence in treader:
    sequence = sequence.upper()
    for i in range(0,len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for position,identity in kmers[kmer]:
                print(kmer,position, identity)
#for kmer, count in sorted(kmers.items(), key=lambda t: t[1]):