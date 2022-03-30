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

# These are the fields we want to update, in this case the internal administration fields for Metadata Steward and Center, Institute, or Office
# Do not replicate this code, by using {} empty brackets under "Common Core," you will erase all fields under Commmon Core
data = """
{
"category": "NCHS",
"license": "Public Domain U.S. Government",
"attribution": "NCHS/DVS",
"customFields": 
    { "Common Core" : 
        {}, 
      "Internal Administration" : 
        {   "Metadata Steward": "pev9@cdc.gov",
            "Center, Institute, or Office": "NCHS/DVS"
         }
    } 
}
"""

# For each dataset in the array, push the new data to Socrata and print
for uid in uids: 
    response = requests.patch('{}/{}'.format(url, uid),
                          auth=(username, password),
                          headers=headers,
                          # the data has to be passed as a string
                          data=data)
    print(response.json())
