import json
import requests

# This is the full path to the metadata API on the domain that you care about
url = 'https://data.cdc.gov/api/views/metadata/v1'

# This is the unique identifier of the dataset you care about
uids = ['jqg8-ycmh', '3sh4-uqpm', 'hk9y-quqm', '9j2v-jamp', '95ax-ymtc', 'nfuu-hu6j', 'bxq8-mugm', '9dzk-mvmi', '6rkc-nb2q']

# And this is your login information

# API Token
username = 'XXXXXXXXXXXXXXXXXXX'

# API Secret
password = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


headers = {'Content-Type': 'application/json'}

# These are the fields you want to update
data = """
{
"category": "NCHS",
"license": "Public Domain U.S. Government",
"attribution": "NCHS/DVS",
"customFields": 
    { "Common Core" : 
        {"Contact Email": "cdcinfo@cdc.gov",
         "Contact Name": "National Center for Health Statistics",
         "Publisher": "National Center for Health Statistics",
         "Public Access Level": "public",
         "Bureau Code": "009:20",
         "Program Code": "009:020"
         }, 
      "Internal Administration" : 
        {"Center, Institute, or Office": "NCHS/DVS"
         }
    } 
}
"""

for uid in uids: 
    response = requests.patch('{}/{}'.format(url, uid),
                          auth=(username, password),
                          headers=headers,
                          # the data has to be passed as a string
                          data=data)
    print(response.json())

print(response.json())