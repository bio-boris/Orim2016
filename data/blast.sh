#!/usr/bin/env bash

source config.sh
mkdir blast

time ./formatdb.py $LIST_OF_PROTEIN_FILES > formatdb_time

time ./blastall_phytozome.py -i $I -b $B -topHits $TOPHITS -processors $PROCESSORS -eval $EVAL  > blastTime
