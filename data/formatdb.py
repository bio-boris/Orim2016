#!/usr/bin/env python
# Uses Blast 2.2.26 formatdb
import os
import sys
from subprocess import call

#Format All Databases
protein_file = ""
if(len(sys.argv)>1):
    protein_file = sys.argv[1]
else:
    sys.exit("--usage list_of_protein_files")


list_of_protein_files =  open(protein_file).read().splitlines()

for file in list_of_protein_files:
  command = "formatdb -pT -i data/{0}".format(file)
  print command
  call(command,shell=True)
