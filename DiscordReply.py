  #!/usr/bin/env python3

import requests
import json
# import simplejson as json



polygon_queries = "https://raw.githubusercontent.com/med-amiine/polygon_discord_queries/main/src/Polygon_queries.json"


def get_answer_discord():
  response = requests.get(polygon_queries)
  queries = json.loads(response.text)





  data = json.load(response.text)
  print(type(data))
  #print(data['guild'])
  default_count = total = 0
  for default in data['messages']:
      total += 1
      if default['type'] != "":
          default_count += 1
          print("Questions :")
          print('id: ' + default['id'])
          print('type: ' + default['type'])
          print('Content: ' + default['content'])
          for reply in data['messages']:
              if "reference" in reply and default['id'] == reply['reference']['messageId']:
                  print('Answers :')
                  print('id: ' + reply['id'])
                  print('type: ' + reply['type'])
                  print('Content: ' + reply['content'])
                  print(reply['reference']['messageId'])
          print("======")
  print('\n==== Summary ====')
  print('Total count: ' + str(total))
  print('Default messages count: ' + str(default_count))
  print('Reply messages count: ' + str(total-default_count))
  print('Non answered messages: ' + str(default_count-(total-default_count)))





