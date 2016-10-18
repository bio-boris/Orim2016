#!/usr/bin/env python
# Grabs protein files, gff3 files, and annotation files from phytozome

from BeautifulSoup import *
import os
import sys

if(len(sys.argv) > 1):
        xml_file = open(sys.argv[1])
else:
        sys.exit("Need XML File")

print "About to open " + sys.argv[1]
soup = BeautifulSoup(xml_file)


file_tags = soup.findAll('file')


urls= []
for tag in file_tags:
        urls.append(tag['url'])


downloads = []
wanted_files =['synonym.txt','protein.fa.gz','gene.gff3.gz','annotation_info.txt','defline.txt']
for url in urls:
        for ending in wanted_files:
                if ending in url:
                        downloads.append( "http://genome.jgi.doe.gov" + url )


for download in downloads:
        filename = os.path.basename(download)
        print "echo " + filename
        print "wget -c '" + download + "' --load-cookies cookies -O " + filename
