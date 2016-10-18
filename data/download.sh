#!/usr/bin/env sh

source config.sh

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode login=$USER_NAME --data-urlencode password=$USER_PASSWORD -c cookies > result
curl 'http://genome.jgi.doe.gov/ext-api/downloads/get-directory?organism=PhytozomeV11' -b cookies > phytozome11.xml

mkdir data
mkdir blast
./getPhytozomeData.py phytozome11.xml > downloadList
sh downloadList
gunzip *
ls | grep protein.fa$ > $PROTEIN_FILES


