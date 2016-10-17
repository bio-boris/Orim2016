#!/usr/bin/env sh

export USER_NAME=user
export USER_PASSWORD=password

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=$USER_NAME' --data-urlencode 'password=$USER_PASSWORD' -c cookies > result

curl 'http://genome.jgi.doe.gov/ext-api/downloads/get-directory?organism=PhytozomeV11' -b cookies > phytozome11.xml

./getData.py phytozome11.xml > downloadList

sh downloadList


