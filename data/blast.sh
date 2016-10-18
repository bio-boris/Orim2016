#!/usr/bin/env bash

source config.sh
mkdir blast

time ./blastall_phytozome.py -i $I -b $B -topHits $TOPHITS -processors $PROCESSORS -eval $EVAL  > blastTime
