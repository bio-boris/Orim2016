Identify the name of the portal before you can download
You can find that using our JGI Portal List search page. Use any search terms necessary to find the portal you want, click on the "Info" link in the "Resources" column, then make a note of the short portal name in the URL. It is the first path after the web host. For example, in the URL http://genome.jgi.doe.gov/Aurpu_var_sub1/... the portal name to use for API download is "Aurpu_var_sub1"

You can also export the full search results into CSV format by clicking Export to Excel, then you could iterate over all your projects.

Log in using the following command.
curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=USER_NAME' --data-urlencode 'password=USER_PASSWORD' -c cookies > /dev/null

Replace USER_NAME, USER_PASSWORD with the appropriate values

Download a list of files available for the portal that you are interested in.
For example, for PhytozomeV10 the command will look like this:

curl 'http://genome.jgi.doe.gov/ext-api/downloads/get-directory?organism=PhytozomeV10' -b cookies > files.xml

Find the file that you would like to download in the XML document and download it.
For example, if you look for "Alyrata_107_v1.0.annotation_info.txt", you will find the following entry in the file:

<file label="PhytozomeV10" filename="Alyrata_107_v1.0.annotation_info.txt" size="3 MB" sizeInBytes="3901148" timestamp="Sun Jan 12 17:46:56 PST 2014" url="/ext-api/downloads/get_tape_file?blocking=true&amp;url=/PhytozomeV10/download/_JAMO/53112a9e49607a1be0055980/Alyrata_107_v1.0.annotation_info.txt" project="" library="" md5="b03b5173b0adabe4c0e37f82b4a7a2a1"/>
Then you need to transfer the URL attribute from the entry to the download curl command (please make sure you that you replace "&amp;" with "&"). The command to download the file would look like this:

curl 'http://genome.jgi.doe.gov/ext-api/downloads/get_tape_file?blocking=true&url=/PhytozomeV10/download/_JAMO/53112a9e49607a1be0055980/Alyrata_107_v1.0.annotation_info.txt' -b cookies > Alyrata_107_v1.0.annotation_info.txt
