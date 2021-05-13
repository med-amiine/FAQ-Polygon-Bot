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

# discord queries channel QnA
polygon_queries = os.environ['polygon_queries']

# defining the api-endpoint / agent / index name
url = "https://bh4d9od16a-dsn.algolia.net/1/indexes/*/queries"
agent = "Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser%20(lite)%3B%20docsearch.js%202.6.3"
index_name =  "matic_developer"

# instance of PolygonSearch
matic_doc_search = PolygonSearch(url,agent,algolia_application_id,algolia_api_key,index_name)

# instance of DiscordReply
polygon_discord_search = DiscordReply(polygon_queries,"api_endpoint","api_key")


# get the result of the doc search
def get_answer_doc(message,results_number):
  matic_result = matic_doc_search.perform_serach(message,results_number)
  #print(matic_result)
  url = [i["url"] for i in matic_result]
  titre = [i["titre"] for i in matic_result]
  return titre,url
  

def get_answer_discord(message,results_number):
  discord_result = polygon_discord_search.perform_serach(message,results_number)
  answer = discord_result[1]
  author = discord_result[0]
  # print(queries)
 
  return answer,author

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
    # answer,author = get_answer_discord(msg,5)
    await message.channel.send("Hi i'm a Polysearch you asked " + msg)
    await message.channel.send("useful link DYOR:")
    for i in range(3):
      await message.channel.send(str(title[i]) + ": " + str(link[i]) + "\n")
    # for i in range(5):
    # await message.channel.send("Another answer from " + str(author[0]) + ": " + str(answer[0]) )
    


client.run(os.environ['TOKEN'])