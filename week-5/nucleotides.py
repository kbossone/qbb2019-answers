#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

class FASTAReader( object ):
   def __init__( self, fh ):
       self.fh = fh
       self.last_ident = None
       self.eof = False
   def next( self ):
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
               sequences.append( line.strip() )
       sequence = "".join( sequences )
       return ident, sequence

reader = FASTAReader(sys.stdin)

while True:
   ident, sequence = reader.next()
   if ident is None:
       break
   print(ident, sequence)