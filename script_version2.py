"""
Script V2
=====
  This script is a simple web scraper that searches for mental disorders on a specific Wikipedia page.
  It collects the names of disorders and their corresponding links, filtering based on user input.
  It is a more focused search compared to the previous version, which used the Wikipedia API.
  
Notes:
  limited scope of topics, searches only this page for things. guerenteed to not return any funny results
  but might have a small scope of understanding since it only scans this page. this thing is very fast
  but if there's something thats not there, we're cooked. god forbid this page is just misinformation.

  i dont know how you would format the JSON request and i assume you
  know how to convert it into a python variable. send me an example JSON and
  you better keep the formatting consistent
"""
userinput = "test"  # example user input, replace with actual input

# imports

import requests
from bs4 import BeautifulSoup
import json

# variables

texts = [] # list of texts
links = [] # list of links

texts_match = [] # texts that match
links_match = [] # corresponding link

tojson = {} # dictionary to export

# constants

RESULTS = 5

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

# convert into a dictionary
count = 0
for a,b in zip(texts_match, links_match):
  tojson[a] = b
  count += 1
  
  if count > (RESULTS - 1):
    break

# export as JSON
file = open(r'results.json', 'w')
file.write("{")
for i in tojson:
  file.write(f'\n  "{i}": "{tojson[i]}"')
  if i != list(tojson.keys())[-1]:
    file.write(",")
file.write("\n}")

# close the file
file.close()