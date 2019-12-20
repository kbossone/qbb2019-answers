#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

arg01 = open(sys.argv[1])
arg02 = open(sys.argv[2])

class FASTAReader(object):

    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False

    def next(self):

        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
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
        seq = "".join(sequences)
        return ident, seq

arg1 = FASTAReader(arg01)
arg2 = FASTAReader(arg02)

prot = {}
nucleo = {}
back_to_nucleo = {}

while True:
    prot_id, prot_seq = arg1.next()
    if prot_id is None:
        break
    prot_id = prot_id.split('_')[0]
    prot[prot_id] = prot_seq
    nucl_id, nucl_seq = arg2.next()
    if nucl_id is None:
        break
    nucleo[nucl_id] = nucl_seq
    
for seq_ID in prot:
    nuc_pos = 0
    nuc_update = ""
    prot_seq = prot[seq_ID]
    nucl_seq = nucleo[seq_ID]
    for char in prot_seq:
        if char == "-":
            nuc_update += "---"
        else:
            nuc_update += nucl_seq[nuc_pos:nuc_pos+3]
            nuc_pos += 3           
    back_to_nucleo[seq_ID] = nuc_update
   
table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    	}

z_score = {}
d_score = []

for i in range(0,len(back_to_nucleo['query']), 3):
   q_codon = back_to_nucleo['query'][i:i+3]
   ds_count = 0
   dn_count= 0
   for ident in back_to_nucleo:
       seq_codon = back_to_nucleo['query'][i:i+3]
       if q_codon != seq_codon:
           if q_codon == '---' or seq_codon == '---':
               continue
           if q_codon not in table or seq_codon not in table:
               continue
           if q_codon == table[seq_codon]:
               ds_count += 1
           else:
               dn_count += 1
   d = dn_count - ds_count
   d_score.append(d)

   
std = np.std(d_score)

for i,d in enumerate(d_score):
    if d > 0:
        z_score[i] = d/std

seqid = []
seqz = []
for key in z_score:
   seqid.append(key)
   value = z_score[key]
   seqz.append(value)    
fig, ax = plt.subplots()   
for i in range(len(z_score)):
    if seqz[i] <= -1.645:
        ax.scatter(i, seqz[i], color="red")
    elif seqz[i] >= 1.645:
        ax.scatter(i, seqz[i], color="red")
    else:
        ax.scatter(i, seqz[i], color="blue")
            
ax.scatter(seqid, seqz)
plt.title ("Sequence Z Scores")
plt.xlabel("Sequence Idenitites")
plt.ylabel("Z Scores")
fig.savefig("z-test.png")
plt.close(fig)