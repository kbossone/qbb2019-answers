#!/usr/bin/env python3

"""
./02-contigs.py <contigs file>
"""

import sys 
import matplotlib.pyplot as plt
import pandas as pd

contigs = open(sys.argv[1])



class FASTAReader(object):
    def __init__(self, fh): 
        self.fh = fh
        self.last_ident = None
        self.eof=False #eof = end of file 
    def next(self):
        if self.eof: #if we have reached the end of the file
            return None, None 
        elif self.last_ident is None: #tells us we are on the first line
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file" 
            ident = line[1:].rstrip("\n") 
        else: 
            ident = self.last_ident
    #if we reached this point, ident is set correctly
        sequences = []
        while True: 
            line = self.fh.readline()
            if line == "":
                self.eof = True 
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n") 
                break
            else: 
                sequences.append(line.strip())
        sequence = "".join(sequences)
        return ident, sequence

reader=FASTAReader(contigs)
# read=FASTAReader(lastz)
contigs= []

while True:
    ident, sequence = reader.next()
    if ident is None:
        break
    # print(ident, sequence, sep = "\t")
    contigs.append(sequence)
sorted_contigs = sorted(contigs, key=len, reverse = True)
total = 0
for i in contigs:
    total += len(i)

average = total/len(contigs)

asc = 0
for i in range(len(contigs)):
    asc += len(sorted_contigs[i])
    if asc >= total/2:
        print("N50 =", len(sorted_contigs[i]))
        break

print(len(contigs))
# print(contigs)

print("Max length =", len(sorted_contigs[0]))
print("Min length =", len(sorted_contigs[-1]))
print("Number of contigs =", len(contigs))
print ("The average length of the contigs =", average)



