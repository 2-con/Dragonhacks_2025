"""DOCSTRING
Dragonhacks competition 2025

Notes:

may be a bit goofy
"""

# imports

import json
import requests
from bs4 import BeautifulSoup
import json
import wikipedia

def search(userinput):
  
  # variables
  packet = {} # the packet itself as a dictionary

  # constants
  DEBUG = False

  # main #########################################

  # variables
  texts = [] # all the list of texts
  links = [] # all the list of links

  texts_match = [] # texts that match
  links_match = [] # corresponding link
  summary_match = [] # summary of the texts that match
  shortened_links = [] # shortened links to avoid conflict

  classifier = []
  answer = {}

  # main

  response = requests.get("https://en.wikipedia.org/wiki/List_of_mental_disorders")
  soup = BeautifulSoup(response.content, 'html.parser')

  for i in soup.find_all('a', href=True):
    href = i['href']
    text = i.text.strip()
    
    if href.startswith('#'):
      continue
    
    if href.startswith('/wiki/'):
      links.append(href)
      texts.append(text)

  # filter for relevant and matching cases
  for a,b in zip(texts, links):
    if userinput in a:
      texts_match.append(a)
      links_match.append(b)

  # shorten to the top 5 results only
  texts_match = texts_match[:5]
  links_match = links_match[:5]

  # shorten links
  for i in links_match:
    shortened_links.append(i.replace('/wiki/', ''))
  
  # fetch summary for the matching texts
  for i in texts_match:
    try: # try getting the summary
      summary_match.append(wikipedia.page(i).summary)
      if DEBUG:
        print(f"grabbing | {i:30} | success")
      
    except: # if error, return error
      summary_match.append("Could not retrieve summary")
      if DEBUG:
        print(f"grabbing | {i:30} | fail")

  # lists of results to process
  classifier = ["texts", "links", "summary"]
  items      = [texts_match, shortened_links, summary_match]

  # appends dictionary
  for a in range(len(classifier)):
    list_ = [] # reset list
    
    # builds a list of items in the thing
    for b in items[a]:
      list_.append(b)
      
    # appends list of items to corresponding class
    answer[classifier[a]] = tuple(list_)
  
  return answer
  
mockJSON = search("autism")
print(mockJSON['summary'][0])