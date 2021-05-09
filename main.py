  #!/usr/bin/env python3

import discord
import os
import requests 
import json
from PolygonSearch import * 
from DiscordReply import *

client = discord.Client()

# credentials for algolia search
algolia_application_id = os.environ['application_id']
algolia_api_key = os.environ['algolia_api_key']

# defining the api-endpoint 
url = "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries"
agent = "Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%20(lite)%3B%20docsearch.js%202.6.3"
index_name =  "matic_developer"

matic_search = PolygonSearch(url,agent,algolia_application_id,algolia_api_key,index_name)

# get the result of the doc search
def get_answer_doc(message,results_number):
  matic_result = matic_search.perform_serach(message,results_number)
  #print(matic_result)
  url = [i["url"] for i in matic_result]
  titre = [i["titre"] for i in matic_result]
  return titre,url
  
polygon_queries = "https://raw.githubusercontent.com/med-amiine/polygon_discord_queries/main/src/Polygon_queries.json"
def get_answer_discord():
  response = requests.get(polygon_queries)
  queries = json.loads(response.text)
  # print(queries)
get_answer_discord()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  print(msg)

  if (msg.startswith('question') or msg.endswith('?') ):
    title,link = get_answer_doc(msg,5)
    await message.channel.send("Hi i'm a Polysearch")
    await message.channel.send("you asked " + msg)
    await message.channel.send("useful link DYOR:")
    #await message.channel.send([str(title[i]) + ": " + str(link[i]) + "\n" for i in range(3)]) 
    for i in range(2):
      await message.channel.send(str(title[i]) + ": " + str(link[i]) + "\n")
    



client.run(os.environ['TOKEN'])