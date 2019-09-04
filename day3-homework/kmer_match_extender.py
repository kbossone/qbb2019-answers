#!/usr/bin/env python3
from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)
k = int(sys.argv[1])
query = "../day3-homework/droYak2_seq.fa"
f = open(query, 'r')
target = "../day3-homework/subset.fa"
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
            for i, ident in kmers[kmer]:
                taseq = tseq[ident]
                tlength = len(taseq)
                qseq = len(sequence)
                extend_right = True
                extended_kmer = kmer
                while extend_right==True:
                    if (i + k == tlength) or (j + k == qseq):
                        if ident in last:
                            last[ident].append((extended_kmer, int(len(extended_kmer))))
                        else:
                            last[ident] = [(extended_kmer, int(len(extended_kmer)))]
                        break
                    if sequence[j + k] == taseq[i + k]:
                        extended_kmer += sequence[j + k]
                        j += 1
                        i += 1
                        
                    else:
                        if ident in last:
                            last[ident].append((extended_kmer, int(len(extended_kmer))))
                        else:
                            last[ident] = [(extended_kmer, int(len(extended_kmer)))]
                        break
for ident in last:
    for extended_kmer in sorted(last[ident], reverse = True, key = lambda t:t[1]):
        print (ident, extended_kmer)
                        
                        
                        