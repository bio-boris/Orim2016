#!/usr/bin/env bash

source config.sh
mkdir blast

time ./formatdb.py $PROTEIN_FILES 
#real	1m48.594s

time ./blastall_phytozome.py -i $I -b $B -topHits $TOPHITS -processors $PROCESSORS -eval $EVAL  
