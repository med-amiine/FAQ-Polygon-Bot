  #!/usr/bin/env python3

import requests
import json

class PolygonSearch:
    
  def __init__(self,api_endpoint,agent,application_id,api_key,index_name):

    self.api_endpoint = api_endpoint
    self.application_id = application_id
    self.api_key = api_key
    self.agent = agent
    self.index_name = index_name
    self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

  def perform_serach(self,search_phrase,number_result):
    params = {'x-algolia-agent': self.agent, 'x-algolia-application-id': self.application_id, 'x-algolia-api-key': self.api_key}

    search_params = "query="+ search_phrase +"&hitsPerPage="+ str(number_result)

    data = {
        "requests": [
            {
                "indexName": self.index_name,
                "params": search_params
            }
        ]
    }

    r = requests.post(self.api_endpoint,params=params, data=json.dumps(data), headers=self.headers)
      
    # extracting response text 
    pastebin_url = r.text
    test = json.loads(pastebin_url)
   
    results = test["results"][0]["hits"]

    res = []
    my_dict = {}
    
    for x in results:
      p= x["url"]
      c = x["hierarchy"]["lvl0"]
      my_dict['url']= p
      my_dict["titre"] = c
      res.append(my_dict.copy())
    return res

def enhance_result():
  # to be added later
  print("cleanning the result...")

