import json
import requests

# This is the full path to the metadata API on the domain that you care about
url = 'https://data.cdc.gov/api/views/metadata/v1'

# These are the unique identifiers 4x4 of the datasets we want to update
uids = ['jqg8-ycmh', '3sh4-uqpm', 'hk9y-quqm', '9j2v-jamp', '95ax-ymtc', 'nfuu-hu6j', 'bxq8-mugm', '9dzk-mvmi', '6rkc-nb2q']

# And this is your login information

# API Token
username = 'XXXXXXXXXXXXXXXXXXX'

# API Secret
password = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


headers = {'Content-Type': 'application/json'}

# This is an example of how I tried to update the "Update Frequency" field
# 1. Do not do this because we want to update the "Update Frequency" field in "Common Core", not in "Data Quality"
# 2. Do not do this because leaving the {} empty brackets for common core and internal admin will erase all fields
data = """
{
"category": "NCHS",
"license": "Public Domain U.S. Government",
"attribution": "NCHS/DVS",
"customFields": 
    { "Common Core" : 
        {}, 
      "Internal Administration" : 
        {},
      "Data Quality" :
        {
            "Update Frequency": "R/P1W"
        }, 
    } 
}
"""

# This pushes the data to Socrata for each dataset in the array, then prints a response each time
for uid in uids: 
    response = requests.patch('{}/{}'.format(url, uid),
                          auth=(username, password),
                          headers=headers,
                          # the data has to be passed as a string
                          data=data)
    print(response.json())