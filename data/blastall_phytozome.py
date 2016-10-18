#!/usr/bin/env python
# Uses Blast 2.2.26 
# Uses Pigz
# Uses list of files
import os

#Get Configs
list_of_protein_files = $config{'protein_files'}
i = $config{$i}


#Format All Databases
for file in list_of_protein_files:
  formatdb -pT file
  mkdir(file + blast)
  
for file in list_of_protein_files:
  directory = file+blast;
  for file2 in list_of_protein_files:
    blast(directory,file,file2)
 


def blast(blast_file):
 # blast with params
 # create time file for blast_time
 i = 5
 d = 5
 o = 5
 top_hits = 10
 output
  

print "About to blast\n";
	my $i = shift ;
	my $d = shift ;
	my $o = shift ;
	my $hits = $Config{'tophits'};
	my $o_temp = "$o.tmp";
	
	my $blast_command ="blastall -p blastp -i $i -d $d " . 
	"-e 1e-5 -m8 -a12 " . 
	"-o $o_temp -b$hits -v$hits -K 1 ";
	print "$blast_command\n";
	system("$blast_command; mv $o_temp $o; pigz -k $o");
  
   def compress(blast_file):
  #pigz compress blast_file
   os.rename(compressed_file + ".tmp", compressed_file)  
