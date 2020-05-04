#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

def sigma(nucs, nuct):
  sig = [[   91, -114,  -31, -123 ],
         [ -114,  100, -125,  -31 ],
         [  -31, -125,  100, -114 ],
         [ -123,  -31, -114,   91 ]]
  nuc = ["A","C","G","T"] 
  st = nucs, nuct
  for nt1 in enumerate(nuc):
    for nt2 in enumerate(nuc):
      index = nt1[0],nt2[0]
      nt12 = nt1[1],nt2[1]
      if st != nt12:
        continue
      elif st == nt12:
        match = index
        score = sig[match[0]][match[1]]
        return score

match_award = 300
mismatch_penalty = -300
gap_penalty = -300
seq1 = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
seq2 = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"

def nwmatrix(seq1, seq2):
    m = len(seq1)  
    n = len(seq2)
    
    dmat = np.zeros((m+1 , n+1), float)
    tmat = np.zeros((m+1 , n+1), int)
   
    for i in range(m + 1):
        dmat[i][0] = gap_penalty * i
    
    for j in range(n + 1):
        dmat[0][j] = gap_penalty * j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dmat[i-1][j-1] + sigma(seq1[i-1],seq2[j-1])
            delete = dmat[i-1][j] + gap_penalty
            insert = dmat[i][j-1] + gap_penalty
            dmat[i][j] = max(match,delete,insert)
    
            if dmat[i][j] == match:
              tmat[i][j] = 1
              
            elif dmat[i][j] == delete: #
              tmat[i][j] = 2
              
            elif dmat[i][j] == insert: #
              tmat[i][j] = 3
              
    return dmat, tmat

def nw( dmat, tmat, s, t ):
  align1 = ''
  align2 = ''
  mutations = ''
  i = len(s)
  j = len(t)
  score = dmat[i][j]
  while i > 0 and j > 0:
    tscore = tmat[i][j]
    if tscore == 1:
        align1 += s[i-1]
        align2 += t[j-1]
        if s[i-1] == t[j-1]:
          mutations += s[i-1]
        elif s[i-1] != t[j-1]:
          mutations += 'X'
        i -= 1
        j -= 1
    elif tscore == 2:
        align1 += s[i-1]
        align2 += '-'
        mutations += '-'
        i -= 1
    elif tscore == 3:
        align1 += '-'
        align2 += t[j-1]
        mutations += '-'
        j -= 1

  align1 = align1[::-1]
  align2 = align2[::-1]
  print ('Sequence 1: ', '\t', align1, '\t', '\n', 'Sequence 2: ', '\t', align2,'\n', 'Mismatched: ', '\t', mutations, '\n', 'Score: ', '\t', str(score))

dmat, tmat = nwmatrix(seq1, seq2)
nw(dmat, tmat, seq1, seq2)