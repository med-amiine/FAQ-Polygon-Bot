#!/usr/bin/env python3

import requests
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# polygon_queries = "https://raw.githubusercontent.com/med-amiine/polygon_discord_queries/main/src/Polygon_queries.json"


class DiscordReply:
    def __init__(self, polygon_queries, api_endpoint, api_key):
        self.polygon_queries = polygon_queries
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def perform_serach(self, search_phrase, number_result):
        response = requests.get(self.polygon_queries)
        # queries = json.loads(response.text)

        data = json.loads(response.text)
        # print(type(data))
        # print(data['guild'])

        fuzz.partial_ratio("this is a test", "this is a test!")

        res = answer_id = []
        my_dict = {}
        default_count = total  = current_score = 0
        score = 1
        for default in data['messages']:
            total += 1
            if default['type'] == "Default":
                default_count += 1
                score = fuzz.partial_ratio(search_phrase, default['content'])
                if score > 80 :
                    print("Similar question :")
                    print('id: ' + default['id'])
                    print('type: ' + default['type'])
                    print('Content: ' + default['content'])
                    print(score)
                    #current_score = score
                    answer_id.append(default['id'])
                    for reply in data['messages']:
                        if "reference" in reply and default['id'] == reply['reference']['messageId']:
                            print('Answer :')
                            print('id: ' + reply['id'])
                            print('type: ' + reply['type'])
                            print('Content: ' + reply['content'])
                            print(reply['reference']['messageId'])
                            my_dict['author']= reply['id']
                            my_dict["titre"] = reply['content']
                            res.append(my_dict.copy())
                        else:
                            res = "404 Not Found: Sorry, your question not found"
                            print(res)
                            return res
                    # Summary of QnA
                    print('\n==== Statistics ====')
                    print('Total count: ' + str(total))
                    print('Default messages count: ' + str(default_count))
                    print('Reply messages count: ' + str(total-default_count))
                    print('Non answered messages: ' + str(default_count-(total-default_count)))


