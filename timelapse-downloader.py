#!/usr/bin/python
import urllib
import urllib2
import json
import os.path
import re


# Get your own API Key at:  http://dashboard.bloomsky.com/user -> left pane -> "Developer"
key = 'YOUR-API-KEY'

# Remove  ?unit=intl  for imperial units
url = 'https://api.bloomsky.com/api/skydata/?unit=intl'

# Provide API-Key in Header an request Data as json
req = urllib2.Request(url)
req.add_header('Authorization', key)
bloomsky_json = urllib2.urlopen(req).read()
bloomsky = json.loads(bloomsky_json)

# Have a look on what was returned?
# print json.dumps(bloomsky, sort_keys=True, indent=4, separators=(',', ': '))

# Loop through all video-Files
for video in bloomsky[0]['VideoList']:

    n = re.search('.*/(.+?)$', video)
    name = n.group(1)

    # The Videos where provided as Fahrenheit and Celsius versions
    # We will add an _C to the filename, because we want the Celsius version
    # Just comment out the following two lines to retrieve the Fahrenheit
    name = re.sub(r".mp4", "_C.mp4", name)
    video= re.sub(r".mp4", "_C.mp4", video)

    # Was the file already downloaded? If yes, then skip.
    if not os.path.isfile(name):
        urllib.urlretrieve (video, name)
        print video + " => " + name
    else:
        print "Skipping: " + name